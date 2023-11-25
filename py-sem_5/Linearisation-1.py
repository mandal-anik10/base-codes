# BVP: Linearisation - 1

import numpy as np
import scipy.linalg as al
import matplotlib.pyplot as plt
from LocalModule.Matrix_Operation import *

C = np.array([[1, 0, 0, 0, 0], [1, -2, 1, 0, 0], [0, 1, -2, 1, 0], [0, 0, 1, -2, 1], [0, 0, 0, 0, 1]])

D = [[100], [0], [0], [0], [20]]

Cin = al.inv(C)

V = M_Multiplication(Cin, D)
print(V)

x_data = np.array([x for x in range(0, 5)])
y_data = []
for i in range(len(V)):
    y_data.append(V[i][0])

plt.plot(x_data, y_data)
plt.xlabel('x value')
plt.ylabel('Temperature')
plt.grid()
plt.show()
