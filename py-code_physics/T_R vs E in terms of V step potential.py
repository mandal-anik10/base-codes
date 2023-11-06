##########################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(0.10, 0.25)

E = np.linspace(0, 15.1, 1000)
V0 = 1
EV = E/V0


def f(IVariable):
    T = []
    R = []
    for i in range(len(IVariable)):
        if IVariable[i]<1:
            t = 0
            r = 1
        else:
            t = 4*((1-1/IVariable[i])**0.5)/(1+(1-1/IVariable[i])**0.5)**2
            r = 1-t
        T.append(t)
        R.append(r)
    return R, T


R, T = f(EV)
Rp, = plt.plot(EV, R, 'c')
Tp, = plt.plot(EV, T, 'orange')

plt.title('Coefficient of Reflection and Transmisssion as a function of E/V')
plt.xlabel('E/V')
plt.ylabel('R(E/V) or T(E/V)')
plt.legend(['Reflection Coefficient', 'Transmission Coefficient'])
plt.xlim([-0.1, 15.1])
plt.ylim([-0.1, 1.1])
plt.grid()

ax.margins(x=0)

vsp = plt.axes([0.10, 0.15, 0.75, 0.03], facecolor='yellow')

sv = Slider(vsp, 'Potential Height', 0.1, 10, valinit=V0)


def update(val):
    V = sv.val
    x_new= E/V
    Rn, Tn = f(x_new)
    Rp.set_ydata(Rn)
    Tp.set_ydata(Tn)

    fig.canvas.draw_idle()


sv.on_changed(update)


plt.show()



