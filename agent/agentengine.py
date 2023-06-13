"""Controller for all agents"""

from world.world import World
from agent.agent import Agent

class AgentEngine:
    def __init__(self, world: World) -> None:
        self.agents : set(Agent) = world.agents

        for agent in self.agents:
            agent.set_observer(self)

    # update method
    def update(self) -> None:
        print("update in engine")
        for agent in self.agents:
            agent.update()
        
    # agents tell engine to update the UI (need a couple more layers)
    def notify(self):
        pass
