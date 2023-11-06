import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import random as rd

fig, ax = plt.subplots()
plt.subplots_adjust(0.55, 0.05)
xx = [0,1,2,3,4,5,6,7,8,9,10]
yy = [0,0,2,4,5,9,3,0,0,0,10]
t0 = 0

def f(xx,yy,t):
    x = []
    y = []
    for i in range(t+1):
        x.append(xx[i])
        y.append(yy[i])
    xn = xx[t]
    yn = yy[t]
    return x,y,xn,yn

x0, y0, xn, yn = f(xx,yy,t0)
l, =plt.plot(x0,y0,'r')
d, =plt.plot(xn,yn,'.k')
plt.fill_between(x0,y0,color='#539ecd')
plt.xlim([-0.25, 10.5])
plt.ylim([-0.25, 10.5])

axt = plt.axes([0.05, 0.05, 0.45, 0.8], facecolor='white')
st = Slider(axt, 'time',0,10,valinit=t0,valstep=1)

def update(val):
    t = int(st.val)
    x,y,xe,ye = f(xx,yy,t)
    l.set_xdata(x)
    l.set_ydata(y)
    plt.fill_between(x,y,color='k')
    d.set_xdata(xe)
    d.set_ydata(ye)

    fig.canvas.draw_idle()
    return x,y
x,y = update(st.val)
st.on_changed(update)

plt.show()