
# DETERMINATION OF THE VALUE OF MAXIMUM, AVERAGE, RMS AND STANDARD DEVIATION OF A GIVEN FUNCTION:

from LocalModule.Integration import *
from LocalModule.Basic import *
import numpy as np

xi = 0
xf = 5

n = 10000

xx = np.linspace(xi, xf, n)
# Suppose,
#    my function is : yi=f(xi)= (x^2)*exp(-x^2)

yy = (xx**2)*np.exp(-xx**2)
zz = np.ones(len(xx))


# MAXIMUM VALUE OF THE FUNCTION:
max = yy[0]
for i in range(len(yy)):
    if max < yy[i]:
        max = yy[i]

print("Maximum value of the function in range ", xi, "to ", xf, " :", max)


# MINIMUM VALUE OF THE FUNCTION:
min = yy[0]
for i in range(len(yy)):
    if min > yy[i]:
        min = yy[i]

print("Minimum value of the function in range ", xi, "to ", xf, " :", min)


# DETERMINATION OF AVG. VALUE:
s = Integrate(yy, xi, xf, n)
z = Integrate(zz, xi, xf, n)

avg = s/z
print("Average value of the function in range ", xi, "to ", xf, " :", avg)


# DETERMINATION OF THE R.M.S VALUE:
sum = Integrate(yy**2, xi, xf, n)
rms = (sum/z)**(1/2)

print("RMS value of the function in range ", xi, "to ", xf, " :", rms)


# DETERMINATION OF THE STANDARD DEVIATION:
v = (yy - avg)**2
add = Sum(v)

sd = (add/(n-1))**0.5

print("Standard deviation of the function in range ", xi, "to ", xf, " :", sd)
