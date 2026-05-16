from typing import Any, Dict


class Blackboard:
    """
    Shared robot state.

    Agents write observations here. The decision engine and verifier
    read from here when proposing or approving actions.
    """

    def __init__(self) -> None:
        self.state: Dict[str, Any] = {}

    def update(self, agent_name: str, data: Dict[str, Any]) -> None:
        self.state[agent_name] = data

    def get_state(self) -> Dict[str, Any]:
        return self.state
