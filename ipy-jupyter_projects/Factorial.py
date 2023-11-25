
# FACTORIAL MODULE:


def Factorial(n, i, step):
    fact = 1
    while i <= n:
        fact = fact*i
        i = i+step
    return fact
