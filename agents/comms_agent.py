from core.agent_base import Agent


class CommsAgent(Agent):
    name = "comms"

    def observe(self):
        return {
            "signal_strength": "weak",
            "earth_contact_window_minutes": 14,
            "last_transmission_minutes_ago": 220,
            "priority_data_waiting": True,
        }
