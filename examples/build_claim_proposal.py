"""
---
title: "Proposal Normalizer Claim Proposal Example"
filetype: "operational"
type: "example"
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
  - "../proposal_normalizer/build_proposal.py"

anchors:
  - "ProposalNormalizer-Example-BuildClaimProposal-v0.1.0"
---
"""

from pathlib import Path
import json

from proposal_normalizer import build_proposal


def main():

    artifact_paths = [
        "claims/claim-001.yaml"
    ]

    mutation = {
        "domain": "claim-lifecycle",
        "resource": "claim",
        "action": "transition",
        "stage": "proposed"
    }

    contract = {
        "id": "claim-lifecycle-policy",
        "version": "0.1.0",
        "hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    }

    actor = {
        "id": "claim-workflow",
        "type": "workflow",
        "declared_role": "proposer"
    }

    run_context = {
        "orchestrator": "alice",
        "reviewers": ["bob"]
    }

    proposal = build_proposal(
        proposal_id="proposal-001",
        actor=actor,
        artifact_paths=artifact_paths,
        mutation=mutation,
        contract=contract,
        run_context=run_context
    )

    print(json.dumps(proposal, indent=2))


if __name__ == "__main__":
    main()
    