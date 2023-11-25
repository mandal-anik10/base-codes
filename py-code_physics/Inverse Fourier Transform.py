# Fourier Transform of a function f(x) to g(K)

from matplotlib.pyplot import *
from numpy import *
from Integration import *

# function
ki = -10
kf = 10
kn = 500
kk = linspace(ki, kf, kn)
aa = kk * pi / 2
gg = ((0.5 * pi ** 3) ** 0.5) * ((sin(aa)) ** 2) / aa ** 2
plot(kk, gg, 'c')

# transformed function
xi = -5
xf = 5
n = 1000
xx = linspace(xi, xf, n)
yy = []

for i in range(len(xx)):
    fi = gg * cos(xx[i] * kk)
    y = Integrate(fi, ki, kf, kn) / (2 * pi) ** 0.5
    yy.append(y)

plot(xx, yy, 'r')
title("Inverse Fourier Transform of a function")
legend(["k-Space(Actual function)", "x-Space(Function after inverse transform)"])
xlabel("k , x")
ylabel("g(k) , f(x)")
grid()
show()
