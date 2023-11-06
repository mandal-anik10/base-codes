
# DETERMINATION OF THE VALUE OF sin(x) WITH ERROR APPROXIMATION :

import math

a = float(input('Angle(in degree): ',))
x = a*math.pi/180.0
eps = float(input('Max error: ',))

(i, fact, s, err, z, tm) = (0.0, 1.0, 0.0, 1.0, 1.0, 0.0)

while err > eps:
    i = i + 1.0
    fact = fact * i

    if i % 2.0 == 1.0:
        z = z+1.0
        t = (x ** i)*((-1.0)**z) / fact
        s = s + t

        err = abs(t)
        tm = tm+1.0

print("\nThe value of the sin(", a, ") with maximum error approximation", eps, " :\t", s)
print("The total number of terms required to reach the accuracy :", tm)
