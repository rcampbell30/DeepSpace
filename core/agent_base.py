from abc import ABC, abstractmethod
from typing import Any, Dict


class Agent(ABC):
    """
    Base class for every narrow specialist agent.

    Each agent observes one part of the robot or environment
    and returns structured information for the blackboard.
    """

    name: str

    @abstractmethod
    def observe(self) -> Dict[str, Any]:
        """Return the agent's current structured observation."""
        raise NotImplementedError
