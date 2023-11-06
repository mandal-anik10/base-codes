# Gram–Schmidt Orthogonalization:

import numpy as np
from LocalModule.Vector_Operation import *

# Initial Vector set
A = np.array([[-1], [2], [3]])
B = np.array([[5], [-6], [7]])
C = np.array([[0], [4], [-8]])

# Orthogonalization:

UA = A
UB = B - (V_Dot(UA, B)/V_Mod(UA))*V_Unit(UA)
UC = C - (V_Dot(UA, C)/V_Mod(UA))*V_Unit(UA) - (V_Dot(UB, C)/V_Mod(UB))*V_Unit(UB)

nUA = V_Unit(UA)
nUB = V_Unit(UB)
nUC = V_Unit(UC)

print(nUA)
print(nUB)
print(nUC)
print(V_Dot(nUA,nUA))