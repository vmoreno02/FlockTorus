"""Driver code that starts the simulation"""
"""When I get my hands on the UI, this will probably be the place to connect it"""

from world.world import World, SPEED
from agent.agentengine import AgentEngine
from threading import Timer

# delta t constant
DELTA_T = 1.0/SPEED

def main():
    world = World()
    engine = AgentEngine(world=world)

    def timed_update():
        engine.update()
        Timer(DELTA_T, timed_update).start()

    timed_update()

if __name__ == "__main__":
    main()