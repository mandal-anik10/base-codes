'''
Spherical Harmonics:

Author : Anik Mandal
'''
## part : 1
import numpy as np
from sympy import *
import math
init_printing(pretty_print=False)

x = symbols('x')

#Associated Legendre Polynomials
def AsLP(variable, lquantum, mquantum):
    LP = diff((variable**2-1)**lquantum, variable, lquantum)/((2**lquantum)*(math.factorial(lquantum)))
    aLP = ((1-variable**2)**(abs(mquantum)/2))*diff(LP, variable, abs(mquantum))
    return aLP

#input
l = 1
m = 0

y=AsLP(x, l, m)
print(y)                 # First run the program, and derive the Associated Legendre function


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


#function:
def f(x):
    y = x               # Copy the function from terminal and paste it here in the place of x and define y, then run again
    return y


if m <= 0:
    esp = 1
    norm = (((4*np.pi/(2*l+1))*(math.factorial(l+abs(m))/math.factorial(l-abs(m))))**0.5)/esp
else:
    esp = (-1)**m
    norm = (((4*np.pi/(2*l+1))*(math.factorial(l+abs(m))/math.factorial(l-abs(m))))**0.5)/esp

FR = f(np.cos(theta))*np.cos(m*phi)/norm
FI = f(np.cos(theta))*np.sin(m*phi)/norm

Mr, mr = FR.max(), FR.min()
Mi, mi = FI.max(), FR.min()
print(Mr,mr)

#plotting:
fig = plt.figure(figsize=plt.figaspect(1),dpi=100)
ax = fig.add_subplot(1,1,1,projection="3d")

CLre = (FR-mr)/(Mr-mr)
CLim = (FI-mi)/(Mi-mi)

ax.plot_surface(xx, yy, zz, rstride=3, cstride=10, facecolors=cm.seismic(CLre))
# ax.set_axis_off()
plt.show()
