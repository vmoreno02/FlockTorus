"""Generates agents... and that's it I think"""

from agent.agent import Agent
from world.vector import Vector
from typing import List
import random, math

# constants
NUM_AGENTS = 5
RADIUS_AGENT = 18
SPEED = 5

class World:
    def __init__(self) -> None:
        # unlike the bee colony, each agent has a starting position (spread out for now)
        self.agents = set()
        positions = self.get_rand_positions()

        print("Behold the agents")
        for i in range(NUM_AGENTS):
            vector = self.get_rand_vec()
            agent = Agent(SPEED, positions[i], vector, i)
            self.agents.add(agent)

    def get_rand_positions(self) -> List:
        positions = []
        space_between = (2 * math.pi) / NUM_AGENTS
        angle = 0

        for i in range(NUM_AGENTS):
            vec = Vector(RADIUS_AGENT, angle)
            positions.append(vec.get_cartesian())
            angle += space_between

        return positions

    def get_rand_vec(self) -> Vector:
        r = 1
        theta = random.uniform(0, (2 * math.pi))
        return Vector(r, theta)