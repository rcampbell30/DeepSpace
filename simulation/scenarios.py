LOW_BATTERY_SCENARIO = {
    "battery": {
        "battery_percent": 12,
        "solar_input": "low",
        "safe_runtime_minutes": 22,
        "status": "danger",
    },
    "terrain": {
        "wheel_slip_risk": "medium",
    },
    "damage": {
        "critical_damage": False,
    },
    "risk": {
        "overall_risk": "medium",
    },
}

HIGH_RISK_TERRAIN_SCENARIO = {
    "battery": {
        "battery_percent": 61,
    },
    "terrain": {
        "wheel_slip_risk": "high",
    },
    "damage": {
        "critical_damage": False,
    },
    "risk": {
        "overall_risk": "high",
    },
}
