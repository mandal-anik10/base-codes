'''
DETERMINATION OF THE SQUARE ROOT OF A GIVEN NUMBER THROUGH BISECTION :

Author : Anik Mandal
'''
x = float(input('Number x: ',))         # x must be positive

a = 0
b = x+10

eps = float(input('Max error : '))
err = 1
tm = 0
d = x + 1
while err > eps:
    c = (a+b)/2

    if c**2 < x:
        a = c
    elif c**2 == x:
        err = eps
    else:
        b = c

    err = abs(c-d)
    d = c
    tm = tm+1
    print("\nThe value of the square root of", x, "is equals to :", d)
print("And the number of terms to reach the accuracy is :", tm)
