from core.agent_base import Agent


class RiskAgent(Agent):
    name = "risk"

    def observe(self):
        return {
            "overall_risk": "medium",
            "main_risk": "battery could drop below safe margin during sample collection",
            "recommended_mode": "cautious",
        }
