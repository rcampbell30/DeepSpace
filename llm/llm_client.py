from typing import Any, Dict


class LLMClient:
    """
    Placeholder for a future LLM reasoning layer.

    The LLM should propose structured plans only. It should never receive
    direct access to robot hardware or action execution.
    """

    def propose_plan(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "action": "hold_position",
            "reason": "LLM client is not connected yet.",
        }
