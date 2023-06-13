"""Handles operations for a single agent"""
"""Includes the math from Dr. Goodrich's paper"""

from world.vector import Vector

class Agent:
    def __init__(self, speed, position, vector: Vector, id: int) -> None:
        self.speed = speed
        self.position = position
        self.vector = vector
        self.id = id
        self.observer = None # to send position back up to UI

    # the function that is called every (delta t), calls the math functions
    def update(self):
        pass

    # repulsion zone vectors
    def repulsion(self):
        pass

    # orientation zone vectors
    def orientation(self):
        pass

    # attraction zone vectors
    def attraction(self):
        pass

    # set engine as observer
    def set_observer(self, observer) -> None:
        self.observer = observer