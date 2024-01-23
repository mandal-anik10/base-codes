'''
Simulating a classical ball inside a box under gravity.
Velocity Distribution

Author : Anik Mandal
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, FuncAnimation

fig = plt.figure(figsize=(10, 5), dpi=100)
ax = fig.add_subplot(1, 2, 1)
ax1 = fig.add_subplot(1, 2, 2)
plt.subplots_adjust(left=0.05, right=0.99)


class Particle:
    def __init__(self, id, position, velocity, acceleration, mass=1, radius=0.1):
        self.id = id
        self.pos = position
        self.vel = velocity
        self.acc = acceleration
        self.mass = mass
        self.rad = radius


def Collision_Det(axis, particle, min, max):
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


def Boundary(ax, x_min, x_max, y_min, y_max):
    ax.plot([x_min, x_max], [y_min, y_min], 'k')
    ax.plot([x_max, x_max], [y_min, y_max], 'k')
    ax.plot([x_max, x_min], [y_max, y_max], 'k')
    ax.plot([x_min, x_min], [y_max, y_min], 'k')


def Window(v, dv, window_n):
    dv = 0.5
    v_n = [i*0 for i in range(window_n)]
    for i in range(window_n):
        s = 0
        if i*dv <= v < (i+1)*dv:
            s = s+1
        v_n[i] = s
    return v_n


p = Particle(1, [[5], [6]], [[25], [-10]], [[0], [-100]])
dt = 0.005
vx, vn = [], []
xmin, xmax, ymin, ymax = 0, 10, 0, 10
dv, w_n = 1, 300


def animate(frame):
    ax.cla()
    ax1.cla()

    ax.set_aspect('equal')
    ax.plot(p.pos[0][0], p.pos[1][0], 'o')
    ax.set_title('Ball inside a box under gravity')
    ax.set_xlim([xmin-0.5,xmax+0.5])
    ax.set_ylim([ymin-0.5, ymax+0.5])
    ax.set_xlabel('x-position')
    ax.set_ylabel('y-position')

    vx = [i*dv for i in range(w_n)]
    v = (p.vel[0][0]**2 + p.vel[1][0]**2)**0.5
    vn = Window(v,dv, w_n)
    ax1.bar(vx, vn, width=dv)
    ax1.set_xlim(20, 150)
    ax1.set_ylim(0, 1.5)
    ax1.grid()

    # floor:
    Boundary(ax, xmin, xmax, ymin, ymax)

    # continuous collision detection
    Collision_Det('x', p, xmin, xmax)
    Collision_Det('y', p, ymin, ymax)

    for i in range(2):
        p.vel[i][0] = p.vel[i][0] + p.acc[i][0] * dt
        p.pos[i][0] = p.pos[i][0] + p.vel[i][0] * dt
    
    if i % 300 == 0:				# for checking animation progress
        print(i / 60, '%' )


ani = FuncAnimation(fig, animate, frames=6000, interval=10)

Writer = FFMpegWriter(fps=100)
print('Running...')
ani.save('outputs/BallInsideBox_VelDist.mp4', writer=Writer)
print('Completed!')

# plt.tight_layout()
plt.show()
