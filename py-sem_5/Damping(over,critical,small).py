# Damping(over, crtical, small): 

import numpy as np
import matplotlib.pyplot as plt

# y'' + 2b *y' + w**2 * y = f(x)    , f(x) = 0

B = [20, 10, 5]

for i in range(len(B)):
    # conditions:
    t0 = 0
    y0 = 0
    yp0 = 2
    f = 100    # w**2

    b=B[i]
    
    ti = t0
    tf = 2
    n = 129
    h = (tf-ti)/(n-1)
    yi = y0
    ypi = yp0
    y2pi = -2*b*ypi-f*yi

    tt = [t0]
    yy = [y0]
    for j in range(1, n):
        ti = ti + h
        yi = yi + h*ypi
        ypi = ypi + h*y2pi
        y2pi = -2 * b * ypi - f * yi

        tt.append(ti)
        yy.append(yi)
    plt.plot(tt, yy)
    tt.clear()
    yy.clear()


plt.legend(["Over damping","Critical damping","Small damping"])
plt.grid()
plt.show()

