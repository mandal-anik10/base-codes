'''
DETERMINATION OF THE VALUE OF π USING RAMANUJAN'S π SERIES

Author : Anik Mandal
'''

import math

s0 = (8 ** 0.5) / 9801                      # constant
(f1, f2, j, k, err, t, c) = (1, 1, 0, 0, 1, 0, 10)
eps = float(input('Max error: ',))
t0 = (1 * (1103 + 26390 * 0)) / (1 * 1)     # 1st term of the summation

'''
as we know that,
    0! = 1
so,
    (4 * 0)! = 1
    pow(0!,4) = 1
and, we also know that,
    pow(396,4*0)= 1
'''
sum = t0

while err > eps:
    t = t + 1
    for i in range(0, t):
        i = i + 1
        p = 4 * i

        f1 = math.factorial(p)
        f2 = math.factorial(i)

        s = (f1 * (1103 + 26390 * i)) / ((f2 ** 4) * (396 ** p))    # every term of the summation
        sum = sum + s                                               # summation part

    pi = 1 / (s0 * sum)

    err = abs(pi - c)
    c = pi

    (f1, f2, sum) = (1, 1, t0)

print("\nApproximated value of π upto :", c)
print("Number of terms required to reach that approximated value :", t + 1)
