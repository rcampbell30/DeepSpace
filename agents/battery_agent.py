from core.agent_base import Agent


class BatteryAgent(Agent):
    name = "battery"

    def observe(self):
        return {
            "battery_percent": 42,
            "solar_input": "moderate",
            "safe_runtime_minutes": 96,
            "status": "stable",
        }
