"""Handles operations for a single agent"""
"""Includes the math from Dr. Goodrich's paper"""

from world.vector import Vector
import math

HEADING_PROPORTIONAL_CONTROLLER_K = 0.5

class Agent:
    def __init__(self, speed, position, vector: Vector, id: int) -> None:
        self.speed = speed
        self.position = position
        self.vector = vector
        self.id = id
        self.observer = None # to send position back up to UI

    # the function that is called every (delta t), calls the math functions
    def update(self):
        # position stuff first (easy part)
        dx = self.position[0] * self.speed
        dy = self.position[1] * self.speed
        
        rep_zone, ori_zone, att_zone = self.observer.get_zones(self)

        rep = self.repulsion(rep_zone)
        ori = self.orientation(ori_zone)
        att = self.attraction(att_zone)

        v1 = rep.add(ori)
        u = v1.add(att)

        ux, uy = u.get_cartesian()
        angular_velocity = HEADING_PROPORTIONAL_CONTROLLER_K * (math.atan2(uy, ux) - self.vector.theta) # TODO: check if right theta

        self.position = (self.position[0] + dx, self.position[1] + dy)
        self.vector.theta += angular_velocity


    # repulsion zone vectors
    def repulsion(self, zone) -> Vector:
        pass

    # orientation zone vectors
    def orientation(self, zone) -> Vector:
        pass

    # attraction zone vectors
    def attraction(self, zone) -> Vector:
        pass

    # set engine as observer
    def set_observer(self, observer) -> None:
        self.observer = observer