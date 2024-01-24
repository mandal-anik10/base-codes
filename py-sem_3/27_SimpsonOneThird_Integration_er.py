'''
DETERMINATION OF THE VALUE OF INTEGRATION OF A FUNCTION THROUGH SIMPSON 1/3 METHOD :

Author : Anik Mandal
'''
import numpy as np

xi = float(input('Initial point: ',))
xf = float(input('Final point: ',))

yi = np.sin(xi) * np.exp((xi ** 3) / 3)
yf = np.sin(xf) * np.exp((xf ** 3) / 3)

# Suppose,
#    my function is : yi=sin(x)*exp(x^3/3)

(n, err, sn, t) = (2, 1, 10, 0)
eps = float(input('Max error: ',))
while err > eps:
    h = (xf-xi)/(n-1.0)

    (i, s) = (1, 0.0)

    while i < (n-1):
        c = xi+i*h
        yc = np.sin(c)*np.exp((c**3)/3)

        if i % 2.0 == 1.0:
            s = s+4.0*yc
        else:
            s = s+2.0*yc
        i = i+1

    n = n+1
    s = (yi+yf+s)*h/3.0

    err = abs(sn-s)
    sn = s
    t += 1

s = sn
print("\nThe value of the integration of my function from", xi, "to", xf, "is equals to : ", s)
print("Number of terms to reach the accuracy : ", t)
