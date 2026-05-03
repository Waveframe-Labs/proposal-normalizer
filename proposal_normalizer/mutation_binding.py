from __future__ import annotations

from typing import Any, Dict, Mapping


REQUIRED_MUTATION_FIELDS = {
    "domain",
    "resource",
    "action",
}


def bind_mutation(mutation: Mapping[str, Any]) -> Dict[str, str]:
    """
    Bind the requested mutation object for proposal assembly.

    The mutation shape is intentionally strict: domain, resource, and
    action are the complete boundary contract.
    """

    missing = [field for field in REQUIRED_MUTATION_FIELDS if field not in mutation]

    if missing:
        raise ValueError("Mutation must include domain, resource, and action")

    normalized: Dict[str, str] = {
        "domain": mutation["domain"],
        "resource": mutation["resource"],
        "action": mutation["action"],
    }

    non_string = [field for field, value in normalized.items() if not isinstance(value, str)]
    if non_string:
        raise ValueError(f"Mutation fields must be strings: {non_string}")

    return normalized
