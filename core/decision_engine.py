from typing import Any, Dict


class DecisionEngine:
    """
    Temporary rule-based decision engine.

    Later this can call an LLM. For now, it creates a simple proposal
    from blackboard state so the whole architecture can be tested.
    """

    def propose_action(self, state: Dict[str, Any]) -> Dict[str, Any]:
        battery = state.get("battery", {})
        science = state.get("science", {})
        risk = state.get("risk", {})
        comms = state.get("comms", {})

        battery_percent = battery.get("battery_percent", 0)
        science_value = science.get("science_value")
        collection_possible = science.get("collection_possible", False)
        overall_risk = risk.get("overall_risk")
        priority_data_waiting = comms.get("priority_data_waiting", False)

        if battery_percent < 25:
            return {
                "action": "enter_low_power_mode",
                "reason": "Battery is below safe operating threshold.",
            }

        if priority_data_waiting and comms.get("earth_contact_window_minutes", 0) > 0:
            return {
                "action": "transmit_priority_data",
                "reason": "Priority data is waiting and a contact window is open.",
            }

        if science_value == "high" and collection_possible and overall_risk != "high":
            return {
                "action": "collect_sample",
                "reason": "High-value sample nearby and risk is acceptable.",
            }

        return {
            "action": "hold_position",
            "reason": "No safe high-priority action is currently available.",
        }
