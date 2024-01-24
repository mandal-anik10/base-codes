'''
BVP: Linearisation - 2
Eq : u''(r) + u'(r)/r - u(r)/r^2 = 0 
BC : u(5) = 0.0038731, u(8) = 0.0030770

Author : Anik Mandal
'''

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

# 1st linear eq : U_1 = 0.0038731
# ith linear eq : U_{i-1} (1/h^2 - 1/(2*xi*h)) + U_i (-2/h^2 - 1/xi^2) + U_{i+1} (1/h^2 + 1/(2*xi*h)) = 0       # from ODE
# last equation : U_n = 0.0030770

for i in range(n):
    for j in range(n):
        if i == j:
            if i == 0 or i == n-1:
                C[0][0] = 1
                C[n-1][n-1] = 1
            else: 
                C[i][j] = -2/h**2-1/vr[i]**2                    # Yn
        elif i == j+1 and i != 0 and i != n-1:
            C[i][j] = 1/h**2-1/(2*vr[i]*h)                        # Yn-1
        elif i == j-1 and i != 0 and i != n-1:
            C[i][j] = 1/h**2+1/(2*vr[i]*h)                         # Yn+1
            
        else:
            C[i][j] = 0
print(C)

D = [[0.0038731], [0], [0], [0], [0.0030770]]

Cin = al.inv(C)

V = np.matmul(Cin, D)
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

