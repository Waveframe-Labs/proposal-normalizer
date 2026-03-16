"""
---
title: "Proposal Normalizer Public Interface"
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
  - "./build_proposal.py"

anchors:
  - "ProposalNormalizer-PublicAPI-v0.1.0"
---
"""

from .build_proposal import build_proposal

__all__ = [
    "build_proposal",
]
