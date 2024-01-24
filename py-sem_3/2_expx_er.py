'''
# DETERMINATION OF THE VALUE OF exp(5) WITH ERROR APPROXIMATION :

Author : Anik Mandal
'''
x = float(input('x: ',))
eps = float(input('Max. error: ',))

(i, fact, s, err, tm) = (0.0, 1.0, 1.0, 1.0, 0.0)

while err > eps:
    i = i + 1.0
    fact = fact*i
    t = (x**i)/fact
    s = s+t

    err = abs(t)
    tm = tm+1.0

print("\nThe value of the exp(", x, ") with maximum approximation", eps, " :\t", s)
print("The total number of terms required to reach the accuracy :", tm)
