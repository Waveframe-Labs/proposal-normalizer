"""
---
title: "Proposal Normalizer Artifact Binding"
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
  - "ProposalNormalizer-ArtifactBinding-v0.1.0"
---
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import List, Dict


def _sha256_file(path: Path) -> str:
    """Compute SHA256 hash of a file."""

    h = hashlib.sha256()

    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)

    return h.hexdigest()


def bind_artifacts(artifact_paths: List[str]) -> List[Dict[str, str]]:
    """
    Produce canonical artifact bindings for a proposal.

    Each artifact entry includes:
        - path
        - sha256
    """

    artifacts: List[Dict[str, str]] = []

    for artifact_path in artifact_paths:

        p = Path(artifact_path)

        if not p.exists():
            raise FileNotFoundError(f"Artifact not found: {artifact_path}")

        sha256 = _sha256_file(p)

        artifacts.append(
            {
                "path": artifact_path,
                "sha256": sha256,
            }
        )

    return artifacts