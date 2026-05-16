from core.agent_base import Agent


class ScienceAgent(Agent):
    name = "science"

    def observe(self):
        return {
            "nearby_sample": "iron-rich rock",
            "science_value": "high",
            "distance_m": 18,
            "collection_possible": True,
        }
