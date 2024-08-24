import numba
import numpy as np
from charge import Charge

class Scene:
    def __init__(self, 
                 charges: list[Charge], 
                 dt: float):
        self.charges = charges
        self.dt = dt