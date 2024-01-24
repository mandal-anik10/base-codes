'''
DETERMINATION OF THE VALUE OF THE (1+x)^n TAYLOR EXPANSION WITH ERROR APPROXIMATION WHEN x<<1

Author : Anik Mandal
'''
x = 0.01
n = 3

eps = 1e-5
(a, s, err, i, f, fn, tm) = (1.0, 1.0, 1.0, 1, 1.0, 1.0, 1)

while err > eps:
    f = f*i
    fn = fn*(n-i+1)

    t = (fn/f)*(x**i)
    s = s+t
    i = i+1

    err = abs(t)
    tm = tm+1

print("\nThe value of (", a, "+", x, ")^", n, " is equals to : ", s)
print("The number of terms to reach the accuracy is :", tm)
