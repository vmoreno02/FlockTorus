"""Controller for all agents"""

from world.world import World
from agent.agent import Agent

#constants
BASE_UNIT = 1  # makes it scalable
RADIUS_OF_REPULSION = 1 * BASE_UNIT
RADIUS_OF_ORIENTATION = 8 * BASE_UNIT
RADIUS_OF_ATTRACTION = 80 * BASE_UNIT # 80 works well to form torus

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
    
    # get all zones in one go
    def get_zones(self, agent):
        rep = set()
        ori = set()
        att = set()

        # repulsion zone
        rep_max_x = agent.position[0] + RADIUS_OF_REPULSION
        rep_min_x = agent.position[0] - RADIUS_OF_REPULSION
        rep_max_y = agent.position[1] + RADIUS_OF_REPULSION
        rep_min_y = agent.position[1] - RADIUS_OF_REPULSION

        # orientation zone
        ori_max_x = agent.position[0] + RADIUS_OF_ORIENTATION
        ori_min_x = agent.position[0] - RADIUS_OF_ORIENTATION
        ori_max_y = agent.position[1] + RADIUS_OF_ORIENTATION
        ori_min_y = agent.position[1] - RADIUS_OF_ORIENTATION

        # attraction zone
        att_max_x = agent.position[0] + RADIUS_OF_ATTRACTION
        att_min_x = agent.position[0] - RADIUS_OF_ATTRACTION
        att_max_y = agent.position[1] + RADIUS_OF_ATTRACTION
        att_min_y = agent.position[1] - RADIUS_OF_ATTRACTION

        for a in self.agents:
            if a is not agent:
                # repulsion zone
                if a.position[0] < rep_max_x and a.position[0] > rep_min_x:
                    if a.position[1] < rep_max_y and a.position[1] > rep_min_y:
                        rep.add(a)
                
                # orientation zone
                elif a.position[0] < ori_max_x and a.position[0] > ori_min_x:
                    if a.position[1] < ori_max_y and a.position[1] > ori_min_y:
                        ori.add(a)

                # attraction zone
                elif a.position[0] < att_max_x and a.position[0] > att_min_x:
                    if a.position[1] < att_max_y and a.position[1] > att_max_y:
                        att.add(a)

        return rep, ori, att


