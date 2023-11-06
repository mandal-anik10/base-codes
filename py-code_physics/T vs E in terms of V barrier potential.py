##########################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(0.10, 0.25)

E = np.linspace(0.0001, 10, 1000)
V0 = 1
EV = E/V0
a0 = 10


def f(x, Ph, Pw):
    T = []
    b = Pw*(Ph)**0.5            # 2m/(hcut**2) = 1
    for i in range(len(x)):
        if x[i] < 1:
            p = (np.sinh(b*(1-x[i])**0.5))**2
            q = 4*x[i]*(1-x[i])
            t = 1/(1+p/q)

        elif x[i] > 1:
            p = (np.sin(b*(x[i]-1)**0.5))**2
            q = 4*x[i]*(x[i]-1)
            t = 1/(1+p/q)

        else:
            p = (b**2)/2
            t = 1/(1+p)

        T.append(t)
    return T


T = f(EV,V0,a0)
Tp, = plt.plot(EV, T, 'r')

plt.title('Barrier Potential: Coefficient Transmisssion as a function of E/V')
plt.xlabel('E/V')
plt.ylabel('T(E/V)')
plt.legend(['Transmission Coefficient '])
plt.xlim([-0.1, 10.1])
plt.ylim([-0.1, 1.1])
plt.grid()

ax.margins(x=0)

vsh = plt.axes([0.10, 0.15, 0.75, 0.03], facecolor='yellow')
asw = plt.axes([0.10, 0.10, 0.75, 0.03], facecolor='yellow')

sh = Slider(vsh, 'Potential Height', 0.1, 10, valinit=V0)
sw = Slider(asw, 'Potential Width\n# 2*m/hcut**2=1', 0, 50, valinit=a0)


def update(val):
    V = sh.val
    a = sw.val
    x_new= E/V
    Tn = f(x_new, V, a)
    Tp.set_ydata(Tn)

    fig.canvas.draw_idle()


sh.on_changed(update)
sw.on_changed(update)


plt.show()



