# Simulating particles in a box to find velocity distribution law
# By Anik Mandal

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
import sys
sys.path.append('/home/anik/git/unipy')
from unipy.Vector_Operation import *  # Local module, you have to have source code of the module to run the code
import numpy as np
import time

fig = plt.figure(figsize=(16, 9))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

Temp = 273 + 1000  # in absolute scale
R = 8.314
M = 0.015  # Molar mass (in kg per mole)
v_avg = ((np.pi * R * Temp) / (2 * M)) ** 0.5  # in m/s (initially, all particle will have same avg velocity)

xmin, ymin, xmax, ymax = 0, 0, 10, 10

n = 250  # number of particles
dv = 20
v_list = np.array([dv * i for i in range(60)])
pp = []
dt = 0.00005  # s
trail_x, trail_y = [], []
sum_n = np.array([0 for i in range(len(v_list))])


class Particle:
    def __init__(self, id, position_vector, velocity_vector, mass=M / (6.023 * 10 ** (26)), radius=0.1):
        self.id, self.pos, self.vel, self.mass, self.rad = id, position_vector, velocity_vector, mass, radius


def Boundary(x_min, y_min, x_max, y_max):
    ax1.plot([x_min, x_max], [y_min, y_min], '-k')
    ax1.plot([x_max, x_max], [y_min, y_max], '-k')
    ax1.plot([x_max, x_min], [y_max, y_max], '-k')
    ax1.plot([x_min, x_min], [y_max, y_min], '-k')


def Wall_Collision_Det(axis, particle, min, max):
    if axis == 'x':
        pi = particle.pos[0][0]
        v = particle.vel[0][0]
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
        v = particle.vel[1][0]
        dx = v * dt
        pf = particle.pos[1][0] + dx
        if pi >= particle.rad - min > pf:
            particle.pos[1][0] = 2 * particle.rad - particle.pos[1][0]
            particle.vel[1][0] = -particle.vel[1][0]

        elif pi <= max - particle.rad < pf:
            particle.pos[1][0] = 2 * (max - particle.rad) - particle.pos[1][0]
            particle.vel[1][0] = -particle.vel[1][0]


def PP_Collision_Det(particle_a, particle_b):  # there are two problems, have to fix!
    dis_v = V_Subtract(particle_b.pos, particle_a.pos, 2)
    dis = V_Mod(dis_v, 2)
    a_nxt, b_nxt = [], []
    for i in range(2):
        a_nxt.append([particle_a.pos[i][0] + particle_a.vel[i][0] * dt])
        b_nxt.append([particle_b.pos[i][0] + particle_b.vel[i][0] * dt])
    dis_nxt = V_Mod(V_Subtract(a_nxt, b_nxt, 2), 2)

    if 2 * particle_a.rad > dis > dis_nxt:
        v_rel_ba = V_Subtract(particle_b.vel, particle_a.vel, 2)
        p_rel_ba = V_Subtract(particle_b.pos, particle_a.pos, 2)
        unit_rel_ba = V_Unit(p_rel_ba, 2)
        Comp = V_Dot(v_rel_ba, unit_rel_ba, 2)

        particle_a.vel = V_Subtract(particle_a.vel, V_Scale(Comp, V_Neg(unit_rel_ba, 2), 2), 2)
        particle_b.vel = V_Subtract(particle_b.vel, V_Scale(Comp, unit_rel_ba, 2), 2)


def Set_axis(ax1, ax2, frame):
    ax1.cla()
    ax2.cla()
    ax1.set_aspect('equal')
    ax1.set_title('Particles inside a 2D box\nNumber of particles: ' + str(n) + '; Sim_speed: ' + str(dt / 0.01) + 's')
    ax1.set_xlabel('x-position')
    ax1.set_ylabel('y-position')
    ax2.set_ylim([0, 10])
    ax2.set_title('Time Avg. Velocity Distribution\nTemp: ' + str(Temp - 273) + '℃')
    ax2.set_xlabel('Velocity(m/s)')
    ax2.set_ylabel('number of particles')
    time_text = ax2.text(600, 9, 'Simulation Time %.2fms' % (frame * 0.05))


# Creating particles:
for i in range(n):
    px = xmax * np.random.uniform(0.01, 0.99)
    py = ymax * np.random.uniform(0.01, 0.99)
    angle = np.random.uniform(0, 2 * np.pi)
    [vx, vy] = [v_avg * np.cos(angle), v_avg * np.sin(angle)]
    p = Particle(id=i + 1, position_vector=[[px], [py]], velocity_vector=[[vx], [vy]])
    pp.append(p)


def animate(frame):
    Set_axis(ax1, ax2, frame)
    Boundary(xmin, ymin, xmax, ymax)

    xx, yy, vv, nn = [], [], [], []
    trail_x.append(pp[0].pos[0][0])
    trail_y.append(pp[0].pos[1][0])

    for i in range(n):
        for j in range(i + 1, n):
            PP_Collision_Det(pp[i], pp[j])

        Wall_Collision_Det('x', pp[i], xmin, xmax)
        Wall_Collision_Det('y', pp[i], ymin, ymax)

        xx.append(pp[i].pos[0][0])
        yy.append(pp[i].pos[1][0])
        pp[i].pos[0][0] = pp[i].pos[0][0] + pp[i].vel[0][0] * dt
        pp[i].pos[1][0] = pp[i].pos[1][0] + pp[i].vel[1][0] * dt

    for i in range(len(v_list)):
        c = 0
        for j in range(n):
            v = V_Mod(pp[j].vel, 2)
            if v_list[i] <= v < v_list[i] + dv:
                c = c + 1
        nn.append(c)

    ax1.plot(xx, yy, '.r')
    ax1.plot(trail_x, trail_y, '-c')

    f_eq = 300  # Assuming after 300 frames the equilibrium will establish(you can change)
    if frame > f_eq:
        for i in range(len(nn)):
            sum_n[i] = sum_n[i] + nn[i]

        n_data = np.array(sum_n) / (frame - f_eq)
        ax2.bar(v_list, n_data, width=dv * 0.8, align='edge')
    if frame % 300 == 0:
        dur = time.time() - ti
        print(frame / 60, '%\t', dur, 's')


ti = time.time()
print('Running...')
ani = FuncAnimation(fig, animate, frames=6000, interval=10)
wr = FFMpegWriter(fps=100)
# ani.save(r'C:\Users\Anik Mandal\Videos\PY3 Videos\Velocity Distribution.mp4', writer=wr)  # Don't forget to change location
tf = time.time()
print('Completed!\nTotal rendering time: ', (tf - ti) / 60, 'min.')

plt.show()