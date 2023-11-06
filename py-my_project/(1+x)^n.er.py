# DETERMINATION OF THE VALUE OF THE (1+x)^n TAYLOR EXPANSION WITH ERROR APPROXIMATION WHEN x<<1


print("\n\tDETERMINATION OF THE VALUE OF THE (1+x)^n TAYLOR EXPANSION WITH ERROR APPROXIMATION WHEN x<<1\n\n")

x = float(input("Please, Enter the value of 'x' as extra fractional part : "))
n = float(input("Please, Enter the value of 'n' as the power of (1+x) : "))

esp = float(input("Please, Enter the value of maximum absolute value of error :"))
(a, s, err, i, f, fn) = (1, 1, 1, 1, 1, 1)

while err > esp:
    f = f * i
    fn = fn * (n - i + 1)
    t = (fn / f) * (x ** i)
    s = s + t
    i = i + 1
    err = abs(t)

print("\nThe value of (", a, "+", x, ")^", n, " is equals to : ", s)
