import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, FuncAnimation

fig = plt.figure(figsize=(16, 9), dpi=100)
ax = fig.add_subplot(1, 2, 1)
ax1 = fig.add_subplot(2, 4, 3)
ax2 = fig.add_subplot(2, 4, 4)
ax3 = fig.add_subplot(2, 4, 7)
ax4 = fig.add_subplot(2, 4, 8)
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


p = Particle(1, [[5], [6]], [[15], [-10]], [[0], [-10]])
dt = 0.001
px, py, vx, vy, tt = [], [], [], [], []
xmin, xmax, ymin, ymax = 0, 10, 0, 10


def animate(frame):
    ax.cla()
    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()

    ax.set_aspect('equal')
    ax.plot(p.pos[0][0], p.pos[1][0], 'o')
    ax.set_title('Ball inside a box under gravity')
    ax.set_xlim([xmin-0.5,xmax+0.5])
    ax.set_ylim([ymin-0.5, ymax+0.5])
    ax.set_xlabel('x-position')
    ax.set_ylabel('y-position')

    tt.append(frame/100)

    px.append(p.pos[0][0])
    ax1.plot(tt, px, 'r')
    ax1.set_xlim([0, 60])
    ax1.set_ylim([-1, 11])
    ax1.set_xlabel('time(s)')
    ax1.set_ylabel('x-position')

    py.append(p.pos[1][0])
    ax2.plot(tt, py, 'r')
    ax2.set_xlim([0, 60])
    ax2.set_ylim([-1, 11])
    ax2.set_xlabel('time(s)')
    ax2.set_ylabel('y-position')

    vx.append(p.vel[0][0])
    ax3.plot(tt, vx, 'g')
    ax3.set_xlim([0, 60])
    ax3.set_ylim([-20, 20])
    ax3.set_xlabel('time(s)')
    ax3.set_ylabel('x-velocity')

    vy.append(p.vel[1][0])
    ax4.plot(tt, vy, 'g')
    ax4.set_xlim([0, 60])
    ax4.set_ylim([-20, 20])
    ax4.set_xlabel('time(s)')
    ax4.set_ylabel('y-velocity')

    # floor:
    Boundary(ax, xmin, xmax, ymin, ymax)

    # continuous collision detection
    Collision_Det('x', p, xmin, xmax)
    Collision_Det('y', p, ymin, ymax)

    for i in range(2):
        p.vel[i][0] = p.vel[i][0] + p.acc[i][0] * dt
        p.pos[i][0] = p.pos[i][0] + p.vel[i][0] * dt


ani = FuncAnimation(fig, animate, frames=6000, interval=10)

Writer = FFMpegWriter(fps=100)
# print('Running...')
# ani.save(r'C:\Users\Anik Mandal\Videos\PY3 Videos\simple collision.mp4', writer=Writer)
# print('Completed!')

# plt.tight_layout()
plt.show()
