# Determination of inertia tensor(Ex2 with Module):

import numpy as np
from LocalModule.Inertia_Tensor import *

M = [1, 0.5, 2]
pos = [[1, 0, 0], [0, 1, 2], [0, 2, 1]]

IT = Inertia_T(M, pos)

print(IT)
