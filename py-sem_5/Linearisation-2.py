#BVP: Linearisation - 1

from LocalModule.Matrix_Operation import *
import numpy as np
import scipy.linalg as al
import matplotlib.pyplot as plt

xi = 5
xf = 8
n = 5
vr = np.linspace(xi, xf, n)
h = (xf-xi)/(n-1)
print(h, vr)
C = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i == j:
            if i == 0 or i == n-1:
                C[0][0] = 1
                C[n-1][n-1] = 1
            else:
                C[i][j] = -2/h**2-1/vr[i]**2                    # Yn
        elif i == j+1 and i != 0 and i != n-1:
            C[i][j] = 1/h**2-1/(vr[i]*h)                        # Yn-1
        elif i == j-1 and i != 0 and i != n-1:
            C[i][j] = 1/h**2+1/(vr[i]*h)                         # Yn+1
            
        else:
            C[i][j] = 0
print(C)

D = [[0.0038731], [0], [0], [0], [0.0030770]]

Cin = al.inv(C)

V = M_Multiplication(Cin, D)
print(V)

x_data = vr
y_data = []
for i in range(len(V)):
    y_data.append(V[i][0])

plt.plot(x_data,y_data)
plt.xlabel('r value')
plt.ylabel('u')
plt.grid()
plt.show()

