import numba
import numpy as np

class Force:
    def __init__(self, force_function):
        self.force_function = force_function

class Charge:
    def __init__(self, 
                 charge: float, 
                 position: np.ndarray, 
                 forces: list[Force]):
        self.charge = charge
        self.position = position
        self.forces = forces
