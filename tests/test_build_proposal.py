from pathlib import Path

from proposal_normalizer import build_proposal


def test_build_proposal_structure(tmp_path: Path):

    artifact = tmp_path / "claim.yaml"
    artifact.write_text("example claim")

    mutation = {
        "domain": "claim-lifecycle",
        "resource": "claim",
        "action": "transition",
    }

    contract = {
        "id": "claim-policy",
        "version": "0.1.0",
        "hash": "a" * 64,
    }

    actor = {
        "id": "workflow",
        "type": "workflow",
        "role": "proposer",
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
