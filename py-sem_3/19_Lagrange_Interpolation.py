'''
DETERMINATION OF THE FUNCTION THROUGH SOME GIVEN POINTS:

Author : Anik Mandal
'''

import matplotlib.pyplot as plt
import numpy as np

# GIVEN POINTS:
x = np.array([-5, -3, -1, 0, 1, 2, 4, 5])
y = np.array([-18, -1, 5, 3, 0, 10, -10, 12])

# DETERMINATION OF THE COEFFICIENTS:
cc = []
print("My points are:")
for i in range(len(x)):
    p = 1
    for j in range(len(x)):
        if j != i:
            p = p*(x[i] - x[j])
    c = y[i]/p
    cc.append(c)
    print("(", x[i], ",", y[i], "), ", end="")
print("\nThe coefficients are : ", cc)

# DETERMINATION OF THE FUNCTION:
def f(ind):
    s = 0
    for k in range(len(x)):
        m = 1
        for j in range(len(x)):
            if j != k:
                m = m * (ind - x[j])
        s = s + cc[k] * m
    return s


xx = np.linspace(x[0], x[-1], 1000)
yy = []
for i in range(len(xx)):
    sum = f(xx[i])
    yy.append(sum)

#DETERMINATION OF THE VALUE OF THE FUNCTION AT A GIVEN POINT:
a = 3.45
b = f(a)
print("So, the value of the function at x=", a, " is : ", b)

plt.plot(x, y, '*r')
plt.plot(xx, yy)
plt.suptitle("DETERMINATION OF THE FUNCTION THROUGH SOME GIVEN POINTS:")
plt.legend(["Given Points","Determined Function"])
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.grid()
plt.show()
