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


def bind_mutation(mutation: Mapping[str, Any]) -> Dict[str, str]:
    """
    Bind the requested mutation object for proposal assembly.

    The mutation shape is intentionally strict: domain, resource, and
    action are the complete boundary contract.
    """

    missing = [field for field in REQUIRED_MUTATION_FIELDS if field not in mutation]

    if missing:
        raise ValueError("Mutation must include domain, resource, and action")

    normalized: Dict[str, str] = {
        "domain": mutation["domain"],
        "resource": mutation["resource"],
        "action": mutation["action"],
    }

    non_string = [field for field, value in normalized.items() if not isinstance(value, str)]
    if non_string:
        raise ValueError(f"Mutation fields must be strings: {non_string}")

    return normalized
