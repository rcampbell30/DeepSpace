from core.agent_base import Agent


class NavigationAgent(Agent):
    name = "navigation"

    def observe(self):
        return {
            "current_position": {"x": 12, "y": 7},
            "target_position": {"x": 40, "y": 19},
            "distance_to_target_m": 31,
            "safe_route_available": True,
        }
