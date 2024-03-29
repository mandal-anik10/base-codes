'''
Shooting method for solving BVP

Author : Anik Mandal
'''

import numpy as np
import matplotlib.pyplot as plt

# Boundary conditions:
x_1 = -1
x1 = 1
y_1 = 1/(np.exp(1)+np.exp(-1))
y1 = y_1

def y2p(x, y, yp):      
    p2 = -y + 2*(yp**2)/y       #ODE
    return p2

n = 1+2**5
h = (x1-x_1)/(n-1)

def Euler_Approx(xi, yi, alp):
    # performs Euler approximation for a given slope/alpha value
    xn = xi
    yn = yi
    ypn = alp
    y2pn = y2p(xn, yn, ypn)
    xx = [xi]
    yy = [yi]

    for i in range(1, n):
        xn = xn+h
        yn = yn + ypn*h
        ypn = ypn + y2pn*h
        y2pn = y2p(xn, yn, ypn)
        yy.append(yn)
        xx.append(xn)
    Y1 = yn
    return [xx, yy, Y1]

alp = np.linspace(0,0.3,1+2**7)
YY = []
for i in range(len(alp)):
    YY.append(Euler_Approx(x_1, y_1, alp[i])[2]-y1)

# print(alp,YY)
# plt.plot(alp,YY)
# plt.xlabel(r'$\alpha (slope)$')
# plt.ylabel('Deviation from the final boundary condition')


# Scanning:
def Find_Closest(arr, target):
    # finds the alpha value of the the closest approch
    pp = np.array(arr)-target
    for i in range(1, len(pp)-1):
        if abs(pp[i]) < abs(pp[i-1]) and abs(pp[i]) < abs(pp[i+1]):
            p = pp[i]
            a = alp[i]
    return a, p

a,p = Find_Closest(YY,0)
print(a,p)


# plotting:
x_data = Euler_Approx(x_1,y_1,a)[0]
y_data = Euler_Approx(x_1,y_1,a)[1]

plt.plot([x_1, x1], [y_1, y1], '*k')
plt.plot(x_data, y_data, 'r')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['Boundary conditions', 'Numerical solution'])
plt.title(r'Solution of BVP using Shooting method: Determined $\alpha$ : {:.3f}'.format(a))

plt.grid()
plt.show()
