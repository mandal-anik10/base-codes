# Fourier Transform of a function f(x) to g(K)

from matplotlib.pyplot import *
from numpy import *
from LocalModule.Integration import *

# function
xi = -15
xf = 15
n = 5000
xx = linspace(xi, xf, n)
yy = []
d = 5
ep = 0.1

for i in range(len(xx)):
    if ep > xx[i]+d/2 > -ep or ep > xx[i]-d/2 > -ep:
        y = 1
    else:
        y = 0
    yy.append(y)
    
plot(xx, yy, 'c')

# transformed function
ki = -15
kf = 15
kn = 1000
kk = linspace(ki, kf, kn)
gg = []

for i in range(len(kk)):
    fi = yy*cos(-kk[i]*xx)
    g = Integrate(fi, xi, xf, n)/(2*pi)**0.5
    gg.append(g)

plot(kk, gg, 'r')
title("Fourier Transform of a function")
legend(["x-Space(actual function)", "k-Space(Transformed function)"])
xlabel("x , k")
ylabel("f(x) , g(k)")
grid()
show()
