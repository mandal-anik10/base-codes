# Spherical Harmonics-Probabilistic Measurement:

## part : 1
import numpy as np
from sympy import *
from Integration import *
from Factorial import *
init_printing(pretty_print=False)

x = symbols('x')

#Associated Legendre Polynomials
def AsLP(variable, lquantum, mquantum):
    LP = diff((variable**2-1)**lquantum, variable, lquantum)/((2**lquantum)*(Factorial(lquantum, 1, 1)))
    aLP = ((1-variable**2)**(abs(mquantum)/2))*diff(LP, variable, abs(mquantum))
    return aLP

#input
l = 1
m = 0

y=AsLP(x, l, m)
print(y)                # First run the program, and derive the Associated Legendre function


## part : 2
import matplotlib.pyplot as plt
from matplotlib import cm,colors
from mpl_toolkits.mplot3d import axes3d

theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

xx = np.sin(theta)*np.cos(phi)
yy = np.sin(theta)*np.sin(phi)
zz = np.cos(theta)


# function:
def f(x):
    y = x               # Copy the function from terminal and paste it here in the place of x and define y, then run again
    return y


if m <= 0:
    esp = 1
    norm = (((4*np.pi/(2*l+1))*(Factorial(l+abs(m),1,1)/Factorial(l-abs(m),1,1)))**0.5)/esp
else:
    esp = (-1)**m
    norm = (((4*np.pi/(2*l+1))*(Factorial(l+abs(m),1,1)/Factorial(l-abs(m),1,1)))**0.5)/esp

P = (f(np.cos(theta))/norm)**2

Mp, mp = P.max(), P.min()
print(Mp, mp)

# plotting:
fig = plt.figure(figsize=plt.figaspect(1),dpi=100)
ax = fig.add_subplot(1,1,1,projection="3d")

CLre = (P - mp) / (Mp - mp)

ax.plot_surface(xx, yy, zz, rstride=1, cstride=1, facecolors=cm.rainbow(CLre))
# ax.set_axis_off()
plt.show()
