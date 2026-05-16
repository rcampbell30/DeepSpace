from core.agent_base import Agent


class TerrainAgent(Agent):
    name = "terrain"

    def observe(self):
        return {
            "slope_degrees": 12,
            "surface": "loose regolith",
            "wheel_slip_risk": "medium",
            "obstacle_detected": False,
        }
