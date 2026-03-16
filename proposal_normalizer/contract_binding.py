"""
---
title: "Proposal Normalizer Contract Binding"
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
  - "ProposalNormalizer-ContractBinding-v0.1.0"
---
"""

from __future__ import annotations

from typing import Any, Dict, Mapping


REQUIRED_CONTRACT_FIELDS = {
    "id",
    "version",
    "hash",
}


def bind_contract(contract: Mapping[str, Any]) -> Dict[str, str]:
    """
    Normalize the contract reference for proposal assembly.

    Ensures that proposals are deterministically bound to a
    specific compiled governance contract artifact.
    """

    missing = REQUIRED_CONTRACT_FIELDS - contract.keys()

    if missing:
        raise ValueError(
            f"Contract object missing required fields: {sorted(missing)}"
        )

    normalized: Dict[str, str] = {
        "id": str(contract["id"]),
        "version": str(contract["version"]),
        "hash": str(contract["hash"]),
    }

    return normalized