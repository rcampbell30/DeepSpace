from core.verifier import Verifier


def test_verifier_rejects_sample_collection_on_high_slip_terrain():
    verifier = Verifier()
    proposal = {
        "action": "collect_sample",
        "reason": "High-value sample nearby.",
    }
    state = {
        "battery": {"battery_percent": 80},
        "terrain": {"wheel_slip_risk": "high"},
        "damage": {"critical_damage": False},
        "risk": {"overall_risk": "medium"},
    }

    assert verifier.approve(proposal, state) is False


def test_verifier_allows_low_power_mode_when_battery_is_low():
    verifier = Verifier()
    proposal = {
        "action": "enter_low_power_mode",
        "reason": "Battery below safe threshold.",
    }
    state = {
        "battery": {"battery_percent": 12},
        "terrain": {"wheel_slip_risk": "medium"},
        "damage": {"critical_damage": False},
        "risk": {"overall_risk": "medium"},
    }

    assert verifier.approve(proposal, state) is True


def test_verifier_rejects_non_safe_action_during_critical_damage():
    verifier = Verifier()
    proposal = {
        "action": "move_to_target",
        "reason": "Target is nearby.",
    }
    state = {
        "battery": {"battery_percent": 75},
        "terrain": {"wheel_slip_risk": "low"},
        "damage": {"critical_damage": True},
        "risk": {"overall_risk": "medium"},
    }

    assert verifier.approve(proposal, state) is False
