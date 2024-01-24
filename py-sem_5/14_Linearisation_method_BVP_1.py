'''
BVP: Linearisation - 1
In this method we find derivatives linear way using `symmetric difference quotient` method.
like, [dy/dx](x=x0) = (y(x0+h)-y(x0-h))/(2h), [d2y/dx2](x=x0) = (y(x0+h)+y(x0-h)-y(x0))/(h^2)
And try to find a set of linear equations from the differential equation. number of the set of 
linear equation depends on the no. of iterations or no. of points to be considered for evaluation.

Eq : T'' = 0
BC : T(0) = 100, T(4) = 20

Author : Anik Mandal
'''
import numpy as np
import scipy.linalg as al
import matplotlib.pyplot as plt


# linear equation : C*V = D, T_{i-1} - 2*T_i + T_{i+1} = 0

C = np.array([[1, 0, 0, 0, 0], [1, -2, 1, 0, 0], [0, 1, -2, 1, 0], [0, 0, 1, -2, 1], [0, 0, 0, 0, 1]])

D = [[100], [0], [0], [0], [20]]

Cin = al.inv(C)

V = np.matmul(Cin, D)
print(V)

x_data = np.array([x for x in range(0, len(D))])
y_data = []
for i in range(len(V)):
    y_data.append(V[i][0])

plt.plot(x_data, y_data)
plt.xlabel('x value')
plt.ylabel('Temperature')
plt.grid()
plt.show()
