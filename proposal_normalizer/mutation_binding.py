"""
---
title: "Proposal Normalizer Mutation Binding"
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

anchors:
  - "ProposalNormalizer-MutationBinding-v0.1.0"
---
"""

from __future__ import annotations

from typing import Any, Dict, Mapping


REQUIRED_MUTATION_FIELDS = {
    "domain",
    "resource",
    "action",
}


def bind_mutation(mutation: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Normalize the requested mutation object for proposal assembly.

    This function validates minimal structural requirements and
    produces a canonical mutation reference suitable for the
    CRI-CORE proposal schema.
    """

    missing = REQUIRED_MUTATION_FIELDS - mutation.keys()

    if missing:
        raise ValueError(
            f"Mutation object missing required fields: {sorted(missing)}"
        )

    normalized: Dict[str, Any] = {
        "domain": mutation["domain"],
        "resource": mutation["resource"],
        "action": mutation["action"],
    }

    # optional lifecycle stage reference
    if "stage" in mutation:
        normalized["stage"] = mutation["stage"]

    return normalized