from __future__ import annotations

from typing import Any, Dict, Mapping


REQUIRED_CONTRACT_FIELDS = {
    "id",
    "version",
    "hash",
}


def bind_contract(contract: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Bind the contract reference for proposal assembly.

    The normalizer validates that the caller supplied a complete
    contract reference. It does not compute, infer, or coerce contract
    truth.
    """

    missing = [field for field in REQUIRED_CONTRACT_FIELDS if field not in contract]

    if missing:
        raise ValueError(f"Contract missing required fields: {missing}")

    return dict(contract)
