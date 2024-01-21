'''
EVALUATION OF THE AREA OF f(x)=exp(-a*x^2) FOR DIFFERENT VALUES OF a :

Author : Anik Mandal
'''

import matplotlib.pyplot as plt
import numpy as np

xi = -5.0
xf = 5.0

a1 = 1.0
a2 = 0.2

n = 10000
h = (xf-xi)/(n-1)

xx = np.linspace(xi, xf, n)
yy1 = np.exp(-a1*xx**2)
yy2 = np.exp(-a2*xx**2)

fxi1 = np.exp(-a1*xi**2)
fxi2 = np.exp(-a2*xi**2)

fxf1 = np.exp(-a1*xf**2)
fxf2 = np.exp(-a2*xf**2)

(s1, s2, i) = (0.0, 0.0, 1)
while i < n-1:
    x = xi+i*h

    fx1 = np.exp(-a1*x**2)
    fx2 = np.exp(-a2*x**2)

    if i % 2 == 0:
        s1 += 4*fx1
        s2 += 4*fx2
    else:
        s1 += 2*fx1
        s2 += 2*fx2
    i += 1
s1 = (fxi1+fxf1+s1)*h/3.0
s2 = (fxi2+fxf2+s2)*h/3.0

print("The value of the integration of exp(-", a1, "*x^2) from", xi, "to", xf, " : ", s1)
print("The value of the integration of exp(-", a2, "*x^2) from", xi, "to", xf, " : ", s2)

plt.plot(xx, yy1, '-.r', xx, yy2, '-.g')

plt.suptitle("PLOTTING OF f(x) = exp(-ax^2) FOR a="+str(a1)+" AND "+str(a2))
plt.title("The values of integrations of f(x) are\n"+str(s1)+" for a = "+str(a1)+" and "+str(s2)+" for a = "+str(a2))
plt.xlabel("x axis")
plt.ylabel("f(x)")
plt.legend(["f(x) = $exp(-"+str(a1)+"x^2)$", "f(x) = $exp(-"+str(a2)+"x^2)$"])
plt.grid()

plt.show()
