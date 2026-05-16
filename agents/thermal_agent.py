from core.agent_base import Agent


class ThermalAgent(Agent):
    name = "thermal"

    def observe(self):
        return {
            "internal_temperature_c": 34,
            "external_temperature_c": -62,
            "heater_required": False,
            "status": "safe",
        }
