import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, FuncAnimation
from LocalModule.Basic import *

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.set_aspect('equal')

xmin, ymin, xmax, ymax = 0, 0, 1, 1


class Particle:
    [px, py, vx, vy] = np.random.random(size=4)

    def __init__(self, id, position=[[px], [py]], velocity=[[vx], [vy]], mass=1, radius=1):
        self.id, self.pos, self.vel, self.mass, self.rad = id, position, velocity, mass, radius


def Boundary(x_min, y_min, x_max, y_max):
    ax1.plot([x_min, x_max], [y_min, y_min], '-k')
    ax1.plot([x_max, x_max], [y_min, y_max], '-k')
    ax1.plot([x_max, x_min], [y_max, y_max], '-k')
    ax1.plot([x_min, x_min], [y_max, y_min], '-k')


def Wall_Collision_Det(axis, particle, min, max):
    if axis == 'x':
        pi = particle.pos[0][0]
        v = particle.vel[0][0] + particle.acc[0][0] * dt
        dx = v * dt
        pf = particle.pos[0][0] + dx
        if pi >= particle.rad - min > pf:
            particle.pos[0][0] = 2 * particle.rad - particle.pos[0][0]
            particle.vel[0][0] = -particle.vel[0][0]

        elif pi <= max - particle.rad < pf:
            particle.pos[0][0] = 2 * (max - particle.rad) - particle.pos[0][0]
            particle.vel[0][0] = -particle.vel[0][0]
    elif axis == 'y':
        pi = particle.pos[1][0]
        v = particle.vel[1][0] + particle.acc[1][0] * dt
        dx = v * dt
        pf = particle.pos[1][0] + dx
        if pi >= particle.rad - min > pf:
            particle.pos[1][0] = 2 * particle.rad - particle.pos[1][0]
            particle.vel[1][0] = -particle.vel[1][0]

        elif pi <= max - particle.rad < pf:
            particle.pos[1][0] = 2 * (max - particle.rad) - particle.pos[1][0]
            particle.vel[1][0] = -particle.vel[1][0]


# def PP_collision_Det():


def Simulate(n):
    x, y = [], []
    for i in range(n):
        p = Particle(id=i)
        x.append(p.pos[0][0])
        y.append(p.pos[1][0])


def animate(frame):
    Boundary(xmin, ymin, xmax, ymax)

    Simulate(10)


ani = FuncAnimation(fig, animate, frames=600, interval=100)
plt.tight_layout()
plt.show()
