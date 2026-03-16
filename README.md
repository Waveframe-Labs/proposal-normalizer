---
title: "Proposal Normalizer — Canonical Proposal Assembly Layer"
filetype: "documentation"
type: "repository-overview"
domain: "governance-integration"
version: "0.1.0"
doi: "TBD"
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
  - "https://waveframelabs.org/schemas/cricore-proposal-0.1.0.json"

anchors:
  - "Proposal-Normalizer-v0.1.0"
  - "Canonical-Proposal-Assembly-Layer"
---

# Proposal Normalizer

Deterministic normalization layer that converts governed domain artifacts into canonical CRI-CORE proposal objects.

## Purpose

Real workflows produce domain artifacts such as:

- claims
- approvals
- decisions
- datasets

CRI-CORE evaluates only a single canonical structure:
```
canonical proposal object
```

The proposal normalizer bridges this boundary.

artifact
↓
mutation reference
↓
proposal normalizer
↓
canonical proposal object
↓
CRI-CORE enforcement


## Responsibilities

The normalizer performs four deterministic operations:

1. **Artifact Binding**

   Computes artifact references and SHA256 hashes.

2. **Mutation Binding**

   Attaches the governed mutation request.

3. **Contract Binding**

   Attaches the compiled governance contract identifier and hash.

4. **Proposal Assembly**

   Produces a canonical proposal object that conforms to the CRI-CORE proposal schema.

## Design Constraints

The normalizer intentionally remains minimal.

It does **not**:

- interpret governance policy
- enforce lifecycle rules
- perform approvals
- evaluate proposal correctness

Those responsibilities belong to **CRI-CORE**.

## Output

The normalizer produces a deterministic proposal envelope suitable for evaluation by the CRI-CORE enforcement pipeline.

<div align="center">
  <sub>© 2026 Waveframe Labs — Independent Open-Science Research Entity</sub>
</div>