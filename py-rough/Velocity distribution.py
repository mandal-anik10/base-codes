# Simulating particles in a box to find velocity distribution law
# By Anik Mandal

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from LocalModule.Vector_Operation import *
from LocalModule.Curve_Fit import Nonlinear_Fit
from warnings import filterwarnings
filterwarnings('ignore')

fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

Temp = 273+30       # in absolute scale
R = 8.314
M = 0.015              # Molar mass (in kg per mole)
v_avg = ((np.pi*R*Temp)/(2*M))**0.5         # in m/s

xmin, ymin, xmax, ymax = 0, 0, 10, 10

n = 250      # number of particles
dv = 20
v_list = np.array([dv * i for i in range(60)])
pp = []
dt = 0.00005           # s
trail_x, trail_y = [], []


class Particle:
    def __init__(self, id, position_vector, velocity_vector, mass=M/(6.023*10**(26)), radius=0.1):
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


def PP_Collisiion_Det(particle_a, particle_b):          # there are two problems, have to fix!
    dis_v = V_Subtract(particle_b.pos, particle_a.pos, 2)
    dis = V_Mod(dis_v, 2)
    a_nxt, b_nxt = [], []
    for i in range(2):
        a_nxt.append([particle_a.pos[i][0] + particle_a.vel[i][0]*dt])
        b_nxt.append([particle_b.pos[i][0] + particle_b.vel[i][0]*dt])
    dis_nxt = V_Mod(V_Subtract(a_nxt, b_nxt, 2), 2)

    if dis < 2 * particle_a.rad and dis > dis_nxt:
        v_rel_ba = V_Subtract(particle_b.vel, particle_a.vel, 2)
        p_rel_ba = V_Subtract(particle_b.pos, particle_a.pos, 2)
        unit_rel_ba = V_Unit(p_rel_ba, 2)
        Comp = V_Dot(v_rel_ba, unit_rel_ba, 2)

        particle_a.vel = V_Subtract(particle_a.vel, V_Scaler(Comp, V_Neg(unit_rel_ba, 2), 2), 2)
        particle_b.vel = V_Subtract(particle_b.vel, V_Scaler(Comp, unit_rel_ba, 2), 2)


def Set_axis(ax1, ax2):
    ax1.cla()
    ax2.cla()
    ax1.set_aspect('equal')
    ax1.set_title('Particles inside a 2D box\nNumber of particles: ' + str(n)+'; Sim_speed: '+str(dt/0.01)+'s')
    ax1.set_xlabel('x-position')
    ax1.set_ylabel('y-position')
    ax2.set_ylim([0,20])
    ax2.set_title('Velocity Distribution\nTemp: '+str(Temp-273)+'℃')
    ax2.set_xlabel('Velocity(m/s)')
    ax2.set_ylabel('number of particles')


# Creating particles:
for i in range(n):
    px = xmax * np.random.uniform(0.01, 0.99)
    py = ymax * np.random.uniform(0.01, 0.99)
    angle = np.random.uniform(0, 2 * np.pi)
    [vx, vy] = [v_avg * np.cos(angle), v_avg * np.sin(angle)]
    p = Particle(id=i+1, position_vector=[[px],[py]], velocity_vector=[[vx], [vy]])
    pp.append(p)


def animate(frame):
    Set_axis(ax1, ax2)
    Boundary(xmin, ymin, xmax, ymax)

    xx, yy, vv, nn = [], [], [], []
    trail_x.append(pp[0].pos[0][0])
    trail_y.append(pp[0].pos[1][0])

    for i in range(n):
        for j in range(i+1, n):
            PP_Collisiion_Det(pp[i], pp[j])

        Wall_Collision_Det('x', pp[i], xmin, xmax)
        Wall_Collision_Det('y', pp[i], ymin, ymax)

        xx.append(pp[i].pos[0][0])
        yy.append(pp[i].pos[1][0])
        pp[i].pos[0][0] = pp[i].pos[0][0] + pp[i].vel[0][0]*dt
        pp[i].pos[1][0] = pp[i].pos[1][0] + pp[i].vel[1][0]*dt

    for i in range(len(v_list)):
        c = 0
        for j in range(n):
            v = V_Mod(pp[j].vel, 2)
            if v_list[i] <= v < v_list[i]+dv:
                c = c + 1
        nn.append(c)


    ax1.plot(xx, yy, '.r')
    ax1.plot(trail_x, trail_y, '-c')
    ax2.bar(v_list, nn, width=dv*0.8, align='edge')

    x_data = v_list[:, None]
    y_data = np.array(nn)[:, None]
    n_p, max_degree, alpha = 216, 10, 0.1
    v_data, n_data = Nonlinear_Fit(x_data, y_data, n_p, max_degree, alpha)
    ax2.plot(v_data, n_data,'-y')
    ax2.legend(['Lasso Regression\nalpha= 0.1; max_degree= 10', 'Simulation Data'])


print('Saving...')
ani = FuncAnimation(fig, animate, frames=3000, interval=10)
# wr = FFMpegWriter(fps=100)
# ani.save(r'C:\Users\Anik Mandal\Videos\PY3 Videos\Collision250_with_mean_graph_small.mp4', writer=wr)
# print('Completed!')

plt.show()
