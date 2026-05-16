from typing import Any, Dict


class Verifier:
    """
    Final safety gate.

    No proposed action should execute unless this approves it.
    """

    def approve(self, proposal: Dict[str, Any], state: Dict[str, Any]) -> bool:
        action = proposal.get("action")
        battery = state.get("battery", {})
        terrain = state.get("terrain", {})
        damage = state.get("damage", {})
        risk = state.get("risk", {})

        battery_percent = battery.get("battery_percent", 0)
        wheel_slip_risk = terrain.get("wheel_slip_risk")
        critical_damage = damage.get("critical_damage", False)
        overall_risk = risk.get("overall_risk")

        safe_actions = {"hold_position", "enter_low_power_mode", "request_help"}

        if critical_damage and action not in safe_actions:
            return False

        if battery_percent < 20 and action not in {"enter_low_power_mode", "hold_position"}:
            return False

        if wheel_slip_risk == "high" and action in {"move_to_target", "collect_sample"}:
            return False

        if overall_risk == "high" and action not in safe_actions:
            return False

        return True
