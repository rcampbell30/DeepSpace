from core.agent_base import Agent


class DamageAgent(Agent):
    name = "damage"

    def observe(self):
        return {
            "wheel_health": "minor wear",
            "arm_health": "nominal",
            "camera_health": "nominal",
            "drill_health": "dust accumulation detected",
            "critical_damage": False,
        }
