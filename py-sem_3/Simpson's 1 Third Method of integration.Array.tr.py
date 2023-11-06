
# DETERMINATION OF THE VALUE OF INTEGRATION OF A FUNCTION THROUGH SIMPSON 1/3 METHOD USING ARRAY:


import numpy as np

print("\n\tDETERMINATION OF THE VALUE OF INTEGRATION OF A FUNCTION THROUGH SIMPSON 1/3 METHOD :\n")


xi = 0.0
xf = 10.0

n = 10000
h = (xf-xi)/(n-1)

xx = np.linspace(xi, xf, n)

# Suppose,
#    my function is : yi=f(xi)=xi^2

yy = xx**2.0

(i, s) = (1, 0.0)

while i < n-1.0:
    k = i % 2.0
    if k == 1.0:
        s = s+4.0*yy[i]
    else:
        s = s+2.0*yy[i]
    i = i+1

s = (yy[0]+yy[n-1]+s)*h/3.0

print("\nThe value of the integration of my function from", xi, "to", xf, "is equals to : ", s)
