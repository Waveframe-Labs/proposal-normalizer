"""
---
title: "Proposal Normalizer Artifact Binding Test"
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
  - "../proposal_normalizer/artifact_binding.py"

anchors:
  - "ProposalNormalizer-TestArtifactBinding-v0.1.0"
---
"""

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