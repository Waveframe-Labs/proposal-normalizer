from pathlib import Path
import json

from proposal_normalizer import build_proposal


def main():

    artifact_paths = [
        "claims/claim-001.yaml"
    ]

    mutation = {
        "domain": "claim-lifecycle",
        "resource": "claim",
        "action": "transition"
    }

    contract = {
        "id": "claim-lifecycle-policy",
        "version": "0.2.0",
        "hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    }

    actor = {
        "id": "claim-workflow",
        "type": "workflow",
        "role": "proposer"
    }

    run_context = {
        "orchestrator": "alice",
        "reviewers": ["bob"]
    }

    proposal = build_proposal(
        proposal_id="proposal-001",
        actor=actor,
        artifact_paths=artifact_paths,
        mutation=mutation,
        contract=contract,
        run_context=run_context
    )

    print(json.dumps(proposal, indent=2))


if __name__ == "__main__":
    main()
    
