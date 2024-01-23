'''
*** Trying to simulate the formation of Super cluster using huge number of particles

Author : Anik Mandal
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from utils import *
import time as t

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1, xlim=[-0.1, 1.1], ylim=[-0.1, 1.1])
ax2 = fig.add_subplot(1, 2, 2)
ax1.set_aspect("equal")
ax2.set_aspect("equal")

# number of particles
n = 500
pp = []
pos = np.random.random((n, 2, 1))  # useful for calculation
vel = np.zeros((n, 2, 1))
acc = np.zeros((n, 2, 1))

px = 100
D = np.zeros([px+2, px+2])

window, = ax1.plot([], [], '.k')


def action(id):
    radi = 0.5
    G = 6.67*10**(-11)
    dt = 0.01
    for i in range(n):
        if id != i:
            rv = V_Subtract(pos[i], pos[id])
            ru = V_Unit(rv)
            r = V_Mod(rv)
            if 0.001 < r <= radi:
                avi = V_Scale(V_Neg(ru), G / r ** 2)
                acc[id] = V_Sum(acc[id], avi)
                vel[id] = V_Sum(vel[id], V_Scale(acc[id], dt))
                pos[id] = V_Sum(pos[id], V_Scale(vel[id], dt))
            elif 0.001 <= r:
                pos[id] = V_Sum(pos[i], V_Scale(ru, 0.01))


def HeatMap(pixel_n, xx, yy):
    f = 1 / pixel_n
    for j in range(pixel_n):
        for k in range(pixel_n):
            count = 0
            for i in range(n):
                if (f * j <= xx[i] < f * (j + 1)) and (f * k <= yy[i] < f * (k + 1)):
                    count = count + 1
            D[j + 1][k + 1] = count
    return D

def animate(frame):
    xp = []
    yp = []
    for i in range(n):
        xp.append(pos[i][0][0])
        yp.append((pos[i][1][0]))
    window.set_data(xp, yp)

    D = HeatMap(px, xp, yp)
    ax2.imshow(D, cmap="afmhot")

    for i in range(n):
        action(i)

    if frame % 60 == 0:
        tn = t.time()
        print(frame/12, "\t", (tn-ti), "s")


ti = t.time()
ani = FuncAnimation(fig, animate, frames=1200, interval=50)
w = FFMpegWriter(fps=20)
f_location = 'outputs/galaxy_cluster_1.mp4'
ani.save(f_location, writer=w)
tf = t.time()
print("Rendering time :", (tf-ti)/60, "min")

plt.show()
