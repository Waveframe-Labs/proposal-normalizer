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
