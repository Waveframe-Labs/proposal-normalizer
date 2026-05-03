from pathlib import Path

import pytest

from proposal_normalizer import build_proposal


def test_contract_passthrough(tmp_path: Path):
    artifact = tmp_path / "artifact.txt"
    artifact.write_text("artifact")

    contract = {
        "id": "c1",
        "version": "1.0.0",
        "hash": "abc123",
    }

    proposal = build_proposal(
        proposal_id="p1",
        actor={
            "id": "a1",
            "type": "workflow",
            "role": "proposer",
        },
        artifact_paths=[str(artifact)],
        mutation={
            "domain": "claims",
            "resource": "claim",
            "action": "transition",
        },
        contract=contract,
    )

    assert proposal["contract"] == contract


def test_missing_contract_hash_fails(tmp_path: Path):
    artifact = tmp_path / "artifact.txt"
    artifact.write_text("artifact")

    contract = {
        "id": "c1",
        "version": "1.0.0",
    }

    with pytest.raises(ValueError):
        build_proposal(
            proposal_id="p1",
            actor={
                "id": "a1",
                "type": "workflow",
                "role": "proposer",
            },
            artifact_paths=[str(artifact)],
            mutation={
                "domain": "claims",
                "resource": "claim",
                "action": "transition",
            },
            contract=contract,
        )
