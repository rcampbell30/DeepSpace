from typing import Any, Dict


class ActionBus:
    """
    Executes approved actions.

    In simulation, this only prints. In a real robot, this would call
    hardware controllers through a constrained interface.
    """

    def execute(self, proposal: Dict[str, Any]) -> None:
        action = proposal.get("action")
        reason = proposal.get("reason")

        print(f"EXECUTING: {action}")
        print(f"REASON: {reason}")
