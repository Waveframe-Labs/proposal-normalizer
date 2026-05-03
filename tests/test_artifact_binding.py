from pathlib import Path

from proposal_normalizer.artifact_binding import bind_artifacts


def test_artifact_binding_generates_sha256(tmp_path: Path):

    f = tmp_path / "artifact.txt"
    f.write_text("test artifact")

    artifacts = bind_artifacts([str(f)])

    assert len(artifacts) == 1

    artifact = artifacts[0]

    assert artifact["path"] == str(f)
    assert len(artifact["sha256"]) == 64
