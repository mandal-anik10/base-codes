
# FOURIER ANALYSIS MODULE(SINGLE FUNCTION):
# IT WILL RETURN COEF. OF SINES, COEF. OF COSINS AND FOURIER FUNCTION:


import numpy as np
from Integration import *

def fourier(y_data, xi, xf, n, nc):
    cc = []
    cs = []
    yy = []

    xx = np.linspace(xi, xf, n)

    for i in range(nc):
        yc = y_data*np.cos(np.pi*i*xx)
        ys = y_data*np.sin(np.pi*i*xx)

        sc = Integrate(yc, xi, xf, n)
        ss = Integrate(ys, xi, xf, n)

        cc.append(sc)
        cs.append(ss)

    cc[0] = cc[0]/2
    yy = []
    zz = np.zeros(n)

    for i in range(n):
        s = 0
        for j in range(nc):
            s = s + cc[j]*np.cos(np.pi*j*xx[i]) + cs[j]*np.sin(np.pi*j*xx[i])

        yy.append(s)
    return cc,cs,yy
