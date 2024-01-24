'''
DETERMINATION OF THE INTEGRATION OF A FUNCTION THROUGH MONTE CARLO RANDOM NUMBER GENERATION METHOD :

Author : Anik Mandal
'''

import random as rd
import matplotlib.pyplot as plt
import numpy as np

n = 100000
ct = 0
ca = 0
xx = []
yy = []
ax = []
ay = []
ux = []
uy = []

# Suppose,
#    my function is : yi=xi^2

for i in range(n):
    x = rd.uniform(-2.0, 2.0)
    y = rd.uniform(0, 1.0)

    xx.append(x)
    yy.append(y)

for i in range(n):
    if np.exp(-(xx[i])**2) >= yy[i]:
        ux.append(xx[i])
        uy.append(yy[i])
        ct += 1.0
    else:
        ax.append(xx[i])
        ay.append(yy[i])
        ca +=1

a = 4.0*1.0
s = (ct/n)*a

plt.plot(ux, uy, '.k', ax, ay, '.r')

plt.suptitle("DETERMINATION OF THE INTEGRATION OF A FUNCTION THROUGH MONTE CARLO RANDOM NUMBER GENERATION METHOD ")
plt.title("Total number of points: "+str(n)+"       The value of the integration : "+str(s))
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend([r"Area under the curve $f(x)=e^{-x^2}$, Number of points:"+str(ct), r"Area above the curve $f(x)=e^{-x^2}$, Number of points:"+str(ca)], loc="upper left")
plt.show()
