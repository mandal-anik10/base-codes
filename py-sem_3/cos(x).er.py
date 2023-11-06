
# DETERMINATION OF THE VALUE OF cos(60) WITH ERROR APPROXIMATION :


import math
print("\n\tDETERMINATION OF THE VALUE OF cos (60) WITH ERROR APPROXIMATION :\n")

a = 60.0
x = a*math.pi/180
eps = 0.00001

(i, fact, s, err, z, tm) = (0.0, 1.0, 1.0, 1.0, 0.0, 0.0)

while err >= eps:
    i = i + 1.0
    fact = fact * i

    if i % 2.0 == 0.0:
        z = z+1
        t = (x ** i)*((-1.0)**z) / fact
        s = s + t

        err = abs(t)
        tm = tm+1.0

print("The value of the cos(", a, ") with maximum error approximation", eps, " :\t", s)
print("The total number of terms required to reach the accuracy :", tm)
