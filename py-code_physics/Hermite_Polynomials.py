# Hermite Polynomials:

import sympy as sp

x = sp.symbols('x')


def H(variable, degree):
    y = ((-1)**degree)*sp.exp(variable**2)*sp.diff(sp.exp(-variable**2), variable, degree)
    return y
