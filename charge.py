import torch
import numpy as np

class Charge:
    def __init__(self, charge, position):
        self.charge = charge
        self.position = position

class Force:
    def __init__(self, force_function):
        self.force_function = force_function