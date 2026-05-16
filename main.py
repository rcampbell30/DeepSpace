from agents.battery_agent import BatteryAgent
from agents.comms_agent import CommsAgent
from agents.damage_agent import DamageAgent
from agents.navigation_agent import NavigationAgent
from agents.risk_agent import RiskAgent
from agents.science_agent import ScienceAgent
from agents.terrain_agent import TerrainAgent
from agents.thermal_agent import ThermalAgent
from core.action_bus import ActionBus
from core.blackboard import Blackboard
from core.decision_engine import DecisionEngine
from core.verifier import Verifier


def collect_agent_observations() -> dict:
    """Run every specialist agent and return the shared state."""
    blackboard = Blackboard()

    agents = [
        BatteryAgent(),
        ThermalAgent(),
        NavigationAgent(),
        TerrainAgent(),
        DamageAgent(),
        ScienceAgent(),
        CommsAgent(),
        RiskAgent(),
    ]

    for agent in agents:
        observation = agent.observe()
        blackboard.update(agent.name, observation)

    return blackboard.get_state()


def main() -> None:
    state = collect_agent_observations()

    decision_engine = DecisionEngine()
    verifier = Verifier()
    action_bus = ActionBus()

    proposal = decision_engine.propose_action(state)

    print("CURRENT STATE:")
    print(state)

    print("\nPROPOSED ACTION:")
    print(proposal)

    if verifier.approve(proposal, state):
        print("\nVERIFIER: approved")
        action_bus.execute(proposal)
    else:
        print("\nVERIFIER: rejected")
        action_bus.execute(
            {
                "action": "hold_position",
                "reason": "Proposed action failed safety verification.",
            }
        )


if __name__ == "__main__":
    main()
