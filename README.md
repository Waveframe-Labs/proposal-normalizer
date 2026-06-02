---
title: "Proposal Normalizer - Canonical Proposal Assembly Layer"
filetype: "documentation"
type: "repository-overview"
domain: "governance-integration"
version: "0.2.0"
doi: "TBD"
status: "Active"
created: "2026-03-16"
updated: "2026-05-03"

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
  - "https://waveframelabs.org/schemas/cricore-proposal-0.2.0.json"

anchors:
  - "Proposal-Normalizer-v0.2.0"
  - "Canonical-Proposal-Assembly-Layer"
---
<p align="center">
  <img src="https://raw.githubusercontent.com/Waveframe-Labs/.github/main/assets/branding/canon_wf_logo_extended.png" width="700">
</p>

# Proposal Normalizer

Strict proposal assembly layer for canonical CRI-CORE proposal objects.

The normalizer binds caller-supplied proposal references into one envelope. It validates boundary shape, computes artifact file hashes, and preserves governance truth supplied by upstream systems.

## Installation

Install from PyPI:

```bash
pip install cricore-proposal-normalizer
```

Requires Python 3.10+.

## Purpose

Real workflows produce:

- artifact files
- actor identity declarations
- mutation requests
- compiled contract references

CRI-CORE evaluates only a single canonical structure:

```text
canonical proposal object
```

The proposal normalizer bridges this boundary.

```text
artifacts + actor + mutation + contract
  -> proposal normalizer
  -> canonical proposal object
  -> CRI-CORE enforcement
```

## Responsibilities

The normalizer performs strict, deterministic binding:

1. **Artifact Binding**

   Verifies each supplied artifact path exists and records its SHA256 hash.

2. **Mutation Binding**

   Requires exactly the mutation boundary shape used by CRI-CORE:

   ```python
   {
       "domain": str,
       "resource": str,
       "action": str,
   }
   ```

3. **Contract Binding**

   Requires a caller-supplied contract reference and preserves it without computing, coercing, or inferring contract truth:

   ```python
   {
       "id": "...",
       "version": "...",
       "hash": "...",
   }
   ```

4. **Actor Binding**

   Requires explicit actor identity, type, and role:

   ```python
   {
       "id": str,
       "type": str,
       "role": str,
   }
   ```

5. **Proposal Assembly**

   Produces a canonical proposal object with no mutation after construction.

## Proposal Shape

```python
{
    "proposal_id": str,
    "timestamp": str,
    "actor": {
        "id": str,
        "type": str,
        "role": str,
    },
    "contract": {
        "id": "...",
        "version": "...",
        "hash": "...",
    },
    "requested_mutation": {
        "domain": str,
        "resource": str,
        "action": str,
    },
    "artifacts": [
        {
            "path": str,
            "sha256": str,
        }
    ],
}
```

When supplied, `run_context` is copied into the proposal envelope.

## Design Constraints

The normalizer is strict, not forgiving. Missing required contract, mutation, or actor fields raise `ValueError`.

It does **not**:

- compute contract hashes
- infer contract identifiers or versions
- infer actor roles
- inject defaults
- accept optional mutation ambiguity
- interpret governance policy
- enforce lifecycle rules
- perform approvals
- evaluate proposal correctness

Those responsibilities belong to **CRI-CORE**.

## Output

The normalizer produces a canonical proposal envelope suitable for evaluation by the CRI-CORE enforcement pipeline.

<div align="center">
  <sub>Copyright 2026 Waveframe Labs - Independent Open-Science Research Entity</sub>
</div>
