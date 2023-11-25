
# DETERMINATION OF THE VALUE OF ln(10) WITH ERROR APPROXIMATION :


print("\n\tDETERMINATION OF THE VALUE OF ln(10) WITH ERROR APPROXIMATION :\n")

a = 10.0

x = 1 - (1/a)

eps = 0.00001
(err, s, i, tm) = (1.0, 0.0, 1.0, 0.0)

while err > eps:
    t = (x**i)/i
    s = s+t
    i = i+1.0

    err = abs(t)
    tm = tm+1.0

print("\nThe value of the ln(", a, ") :  ", s)
print("The total number of terms required to reach the accuracy :", tm)

