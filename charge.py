import numba
import numpy as np

class Force:
    def __init__(self, force_function):
        self.force_function = force_function


class Charge:
    def __init__(self, 
                 charge: float, 
                 mass: float,
                 position: np.ndarray, 
                 forces: list[Force], 
                 grid_shape: tuple):
        self.charge = charge
        self.pos = position
        self.vel = 0
        self.acc = self.forces(self, 0)
        self.mass = mass
        self.forces = forces
        self.pos_history = [self.pos]
        self.acc_history = [self.acc]
        self.grid = np.ndarray(shape = grid_shape)

    def update(self, time, dt):

        self.pos = self.pos + self.vel*dt + self.acc*dt**2/2
        self.vel = self.vel + self.acc*dt
        self.acc = self.forces(self, time)/ self.mass

        self.pos_history.append(self.pos)
        self.acc_history.append(self.acc)

        self.grid = update_grid(time, dt)

        
        
