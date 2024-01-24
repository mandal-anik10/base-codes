'''
Problem given as a homework at HRI : 

Author : Anik Mandal
'''

# problem : 1
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)


def Integrate(yy, i, f, step):      # Simpson 1/3 method of integration
    h = abs(f-i)/(step-1)
    s = 0
    for i in range(1, step-1):
        if i%2 == 1:
            s = s + 4*yy[i]
        else:
            s = s + 2*yy[i]
    s = (yy[0] + s + yy[step-1])*h/3
    return s


N = 2**10                       # N = 2^(T)

k = np.array([i for i in range(0, N)])
t = k/N
f0 = 30                         # given
g = np.sin(2*np.pi*f0*t)

ax1.plot(t, g)
ax1.set_title('Actual Function g vs t')

# Fourier Transform
f = np.linspace(-45, 45, 2**10)
h = []

for i in range(len(f)):
    fi = g*np.cos(2*np.pi*f[i]*t)       # only considering real component
    val = Integrate(fi, t[0], t[-1], len(t))/(2*np.pi)**0.5
    h.append(val)

ax2.plot(f, h)
ax2.set_title('Fourier Transform h vs f')

# Inverse fourier transform
tp = t
gp = []

for i in range(len(t)):
    fi = h*np.cos(2*np.pi*t[i]*f)       # only considering real component
    val = Integrate(fi, f[0], f[-1], len(f))/(2*np.pi)**0.5
    gp.append(val)

ax3.plot(tp, gp)
ax3.set_title('Inverse Fourier Transform g\' vs t\' ')

ax4.plot(t, g, '-y', tp, gp)
ax4.set_title('Comparing Actual and Inv. FT function')

plt.show()
