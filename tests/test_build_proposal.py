"""
---
title: "Proposal Normalizer Proposal Assembly Test"
filetype: "documentation"
type: "test"
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

ai_assisted: "partial"

dependencies:
  - "../proposal_normalizer/build_proposal.py"

anchors:
  - "ProposalNormalizer-TestBuildProposal-v0.1.0"
---
"""

from pathlib import Path

from proposal_normalizer import build_proposal


def test_build_proposal_structure(tmp_path: Path):

    artifact = tmp_path / "claim.yaml"
    artifact.write_text("example claim")

    mutation = {
        "domain": "claim-lifecycle",
        "resource": "claim",
        "action": "transition",
        "stage": "proposed",
    }

    contract = {
        "id": "claim-policy",
        "version": "0.1.0",
        "hash": "a" * 64,
    }

    actor = {
        "id": "workflow",
        "type": "workflow",
        "declared_role": "proposer",
    }

    proposal = build_proposal(
        proposal_id="test-proposal",
        actor=actor,
        artifact_paths=[str(artifact)],
        mutation=mutation,
        contract=contract,
    )

    assert proposal["proposal_id"] == "test-proposal"

    assert "timestamp" in proposal
    assert proposal["actor"]["id"] == "workflow"

    assert proposal["contract"]["id"] == "claim-policy"

    assert proposal["requested_mutation"]["resource"] == "claim"

    assert len(proposal["artifacts"]) == 1