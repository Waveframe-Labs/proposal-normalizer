"""
---
title: "Proposal Normalizer Canonical Proposal Builder"
filetype: "operational"
type: "specification"
domain: "governance-integration"
version: "0.1.0"
doi: "TBD-0.1.0"
status: "Active"
created: "2026-03-16"
updated: "2026-03-16"

author:
  name: "Shawn C. Wright"
  email: "swright@waveframelabs.org"
  orcid: "https://orcid.org/0009-0006-6043-9295"

maintainer:
  name: "Waveframe Labs"
  url: "https://waveframelabs.org"

license: "Apache-2.0"

copyright:
  holder: "Waveframe Labs"
  year: "2026"

ai_assisted: "partial"

dependencies:
  - "./artifact_binding.py"
  - "./mutation_binding.py"
  - "./contract_binding.py"

anchors:
  - "ProposalNormalizer-BuildProposal-v0.1.0"
---
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, Mapping

from .artifact_binding import bind_artifacts
from .mutation_binding import bind_mutation
from .contract_binding import bind_contract


REQUIRED_ACTOR_FIELDS = [
    "id",
    "type",
    "role",
]


def _bind_actor(actor: Mapping[str, Any]) -> Dict[str, str]:
    missing = [field for field in REQUIRED_ACTOR_FIELDS if field not in actor]
    if missing:
        raise ValueError(f"Actor missing required fields: {missing}")

    bound_actor = {
        "id": actor["id"],
        "type": actor["type"],
        "role": actor["role"],
    }

    non_string = [field for field, value in bound_actor.items() if not isinstance(value, str)]
    if non_string:
        raise ValueError(f"Actor fields must be strings: {non_string}")

    return bound_actor


def build_proposal(
    *,
    proposal_id: str,
    actor: Mapping[str, Any],
    artifact_paths: list[str],
    mutation: Mapping[str, Any],
    contract: Mapping[str, Any],
    run_context: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """
    Assemble a canonical CRI-CORE proposal object.

    This function binds caller-supplied proposal references into the
    canonical proposal envelope expected by the CRI-CORE enforcement
    pipeline.
    """

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    bound_actor = _bind_actor(actor)

    artifacts = bind_artifacts(artifact_paths)

    requested_mutation = bind_mutation(mutation)

    contract_binding = bind_contract(contract)

    proposal: Dict[str, Any] = {
        "proposal_id": proposal_id,
        "timestamp": timestamp,
        "actor": bound_actor,
        "contract": contract_binding,
        "requested_mutation": requested_mutation,
        "artifacts": artifacts,
        **({"run_context": dict(run_context)} if run_context is not None else {}),
    }

    return proposal
