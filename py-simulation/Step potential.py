

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(0.10, 0.25)

x = np.linspace(0,30,1000)
xi = np.linspace(0,15,1000)
xr = np.linspace(0,15,1000)
xt = np.linspace(15,30,1000)
V0 = 25
E0 = 50
t0 = 0

## Potential:
def V(z):
    vv = []
    for i in range(len(z)):
        if z[i] < 15:
            v = 0
        else:
            v = V0
        vv.append(v)
    return vv
VV = V(x)
plt.plot(x, VV, 'k')


## Wave Functions:
def Wave(x, t, amplitude, wave_number, direction):
    if direction == 'R':
        y = amplitude * np.sin(wave_number * x) * np.exp(-(x-t)**2)                     # velocity = 1
    if direction == 'L':
        y = amplitude * np.sin(wave_number * x) * np.exp(-(x+t)**2)
    return y


def System(space,time,energy,potential):
    if energy > potential:
        k = energy**0.5
        l = (energy-potential)**0.5
        if time<15:
            IW = Wave(xi, time,amplitude=10, wave_number=k, direction='R')
            RW = Wave(xr, time, amplitude=-10*(k-l)/(k+l), wave_number=k, direction='L')*0
            TW = Wave(xt, time, amplitude=10*2*k/(k+l), wave_number=l, direction='R')*0
        else:
            IW = Wave(xi, time,amplitude=10, wave_number=k, direction='R')*0
            RW = Wave(xr, time, amplitude=-10*(k-l)/(k+l), wave_number=k, direction='L')
            TW = Wave(xt, time, amplitude=10*2*k/(k+l), wave_number=l, direction='R')

    return IW, RW, TW

IW, RW, TW = System(x,t0,E0,V0)

Ip, = plt.plot(xi, IW, 'r')
Rp, = plt.plot(xr, RW, 'c')
Tp, = plt.plot(xt, TW, 'orange')
plt.title('Reflection and Transmission: Step Potential')
plt.xlabel('X')
plt.ylabel('V(x) or Ψ(x)')
plt.legend(['Potential', 'Incident Wave', 'Reflected Wave', 'Transmitted Wave'])
plt.xlim([-5, 35])
plt.ylim([-12, 30])
plt.grid()

ax.margins(x=0)

axt = plt.axes([0.10, 0.15, 0.75, 0.03], facecolor='yellow')
axE = plt.axes([0.10, 0.1, 0.75, 0.03], facecolor='yellow')
axV = plt.axes([0.10, 0.05, 0.75, 0.03], facecolor='yellow')

st = Slider(axt, 'Time', 0, 30, valinit=t0)
sE = Slider(axE, 'Energy', 0, 100, valinit=E0)
sV = Slider(axV, 'Potential',0,100, valinit=V0)

def update(val):
    t = st.val
    E = sE.val
    V = sV.val
    IWn, RWn, TWn = System(x, t, E, V)
    Ip.set_ydata(IWn)
    Rp.set_ydata(RWn)
    Tp.set_ydata(TWn)

    fig.canvas.draw_idle()


st.on_changed(update)
sE.on_changed(update)
sV.on_changed(update)

plt.show()



