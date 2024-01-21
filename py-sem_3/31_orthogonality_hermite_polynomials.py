'''
ORTHOGONALITY OF HERMITE POLYOMIALS:

Author : Anik Mandal
'''
import numpy as np

xi = -100
xf = 100
n = 10000

# HERMITE POLYNOMILS:
#         H0(x) = 1
#         H1(x) = 2x
#         H2(x) = 4x^2-2                  ...(1)
#         H3(x) = 8x^3-12x
#         H4(x) = 16x^4-48x^2+12          ...(2)

xx = np.linspace(-xi, xf, n)

# WEIGHT FUNCTION FOR HERMITE POLYNOMIALS:
#         W(x) = exp(-x^2)

yy = (4*xx**2-2)*(16*xx**4-48*xx**2+12)*np.exp(-xx**2)

s = np.trapz(yy, xx, dx=xx[1]-xx[0])

print("The value of the integration of H2(x)*H4(x)*W(x) from", xi, "to", xf, "equals to: ", s)
