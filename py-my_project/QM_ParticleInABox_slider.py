'''
Plotting Eigenstates of particle inside a box using slider

Author : Anik Mandal
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(0.10, 0.25)

a0 = 1
n0 = 5
delta_n = 1
xx = np.linspace(-0.25, a0+0.5, 1000)


def f(zz, length, qn):
    ff = []
    alp = (2/length)**0.5
    for i in range(len(zz)):
        if zz[i] < 0:
            f = 0
        elif zz[i] > length:
            f = 0
        else:
            f = alp*np.sin(qn*np.pi*zz[i]/length)
        ff.append(f)
    return ff


def V(zz, length):
    ff = []
    for i in range(len(zz)):
        if zz[i] < 0:
            vy = 10
        elif zz[i] > length:
            vy = 10
        else:
            vy = 0
        ff.append(vy)
    return ff


ff = f(xx,a0,n0)
vv = V(xx, a0)
s, = plt.plot(xx, ff, 'c')
v, = plt.plot(xx, vv, 'r')

plt.title('Eigenstates: Particle in a box')
plt.xlabel('x')
plt.ylabel('Ψ(x) or V(x)')
plt.legend(['Individual Eigenstate', 'Potential Function'])
plt.xlim([-0.25, 3.5])
plt.ylim([-1.5, 1.5])
plt.grid()

ax.margins(x=0)

axa = plt.axes([0.10, 0.15, 0.75, 0.03], facecolor='yellow')
axn = plt.axes([0.10, 0.1, 0.75, 0.03], facecolor='yellow')

sa = Slider(axa, 'Well Width', 0, np.pi, valinit=a0)
sn = Slider(axn, 'Quantum Number', 1, 25, valinit=n0, valstep=1)


def update(val):
    a = sa.val
    n = sn.val
    x_new= np.linspace(-0.25, a+0.5, 1000)
    s.set_xdata(x_new)
    s.set_ydata(f(x_new, a, n))

    v.set_xdata(x_new)
    v.set_ydata(V(x_new, a))

    fig.canvas.draw_idle()


sa.on_changed(update)
sn.on_changed(update)

plt.show()



