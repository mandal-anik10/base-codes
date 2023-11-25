
# DETERMINATION OF THE VALUE OF SQUARE ROOT OF A GIVEN NUMBER THROUGH NEWTON-RAPHSON METHOD WITH ERROR APPROXIMATION :

n = float(input('Number n: ',))

x = 10.0
eps = float(input('Max error: ',))
(err, i, tm) = (1.0, 1.0, 0.0)

while err > eps:
    x1 = x
    m = 2.0*x1
    y = (x1**2.0)-n
    x = x1-(y/m)
    z = (x**2.0)-n

    err = abs(y-z)
    tm = tm+1.0

print("The value of square root of", n, "with given accuracy", eps, " is : ", x)
print("The number of terms to reach the accuracy is : ", tm)
