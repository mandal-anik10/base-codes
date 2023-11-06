

import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(0.10, 0.25)

x = np.linspace(-25, 25, 10000)
t0 = 0
v0 = 0
c = 1
gamma = 1/(1-(v0/c)**2)**0.5

def psi(x, t, c, gamma):
    ps = np.sin(gamma*x - c*t)
    return ps

y0 = psi(x, t0, c, 1)
y = y0
plt.plot(x, y0,)
mf, = plt.plot(x, y)
plt.suptitle('Why we need more generalised transformation law for wave equ!')
plt.title('')
plt.legend(['General wave form','1D Wave equation under \nGalilean transformation\n(//Approx.) Wave velocity,c = 1'])
plt.xlabel('Spatial Coordinate(x)')
plt.ylabel(r'$\psi(x,t)$')


ax.margins(x=0)

ts = plt.axes([0.10, 0.15, 0.75, 0.03], facecolor='yellow')
time = Slider(ts, 'Time(s)', 0, 10, valinit=t0)

vs = plt.axes([0.10, 0.10, 0.75, 0.03], facecolor='yellow')
rv  = Slider(vs, 'Relative Velocity\n(in unit c)', -c*0.99, c*0.99, valinit=v0)

def update(val):
    T = time.val
    V = rv.val
    gamma_n = 1/(1-(V/c)**2)**0.5
    y_n = psi(x, T, c, gamma_n)
    mf.set_ydata(y_n)

    fig.canvas.draw_idle()

time.on_changed(update)
rv.on_changed(update)

plt.show()