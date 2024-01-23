'''
Fourier Transform of a function f(x) to g(K)

Author : Anik Mandal
'''
import matplotlib.pyplot as plt
import numpy as np

# function
xi = -15
xf = 15
n = 5000
xx = np.linspace(xi, xf, n)
yy = []
d = 5
ep = 0.1

for i in range(len(xx)):
    if ep > xx[i]+d/2 > -ep or ep > xx[i]-d/2 > -ep:
        y = 1
    else:
        y = 0
    yy.append(y)
    
plt.plot(xx, yy, 'c')

# transformed function
ki = -15
kf = 15
kn = 1000
kk = np.linspace(ki, kf, kn)
gg = []

for i in range(len(kk)):
    fi = yy*np.cos(-kk[i]*xx)
    g = np.trapz(fi, xx, dx=xx[1]-xx[0])/(2*np.pi)**0.5
    gg.append(g)

plt.plot(kk, gg, 'r')
plt.title("Fourier Transform of a function")
plt.legend(["x-Space(actual function)", "k-Space(Transformed function)"])
plt.xlabel("x , k")
plt.ylabel("f(x) , g(k)")
plt.grid()
plt.show()
