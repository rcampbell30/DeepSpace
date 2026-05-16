from typing import Any, Dict


def default_environment() -> Dict[str, Any]:
    """Return a fake planetary environment for early simulation work."""
    return {
        "world": "Mars-like test field",
        "temperature_c": -62,
        "surface": "loose regolith",
        "dust_level": "moderate",
        "visibility": "clear",
        "radiation": "elevated",
    }
