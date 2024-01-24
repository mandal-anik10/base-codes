'''
Simulating motion of Venus respect to moon in the sky

Author : Anik Mandal
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, FuncAnimation
from utils import *


class Object:
    def __init__(self, name, mass, pos, momentum, force=None):
        self.name = name
        self.mass = mass
        self.pos = pos
        self.momentum = momentum
        self.force = force


def Grav_F(on_o, due_to_o):
    G = 1
    r_vec = V_Sum(on_o.pos, V_Neg(due_to_o.pos))
    r_mag = V_Mod(r_vec)
    r_cap = r_vec/r_mag
    f_mag = -G * on_o.mass * due_to_o.mass / r_mag ** 2
    f_vec = f_mag*r_cap
    return f_vec


def Net_F(on_o, o):
    s = 0
    for i in range(len(o)):
        s = s + Grav_F(on_o,o[i])
    return s


# Sun:
sun = Object(name='Sun',
             mass=333000,
             pos=[[0], [0], [0]],
             momentum=[[0], [0], [0]])
# planet:
venus = Object(name='Venus',
               mass=81,
               pos=[[75], [0], [0]],
               momentum=[[0], [5400], [0]])
earth = Object(name='Earth',
               mass=100,
               pos=[[147.1], [0], [0]],
               momentum=[[0], [4800], [0]])
# sub planet:
moon = Object(name='Moon',
              mass=20,
              pos=[[150], [0], [0]],
              momentum=[[0], [1100], [0]])

# plotting:
fig = plt.figure(figsize=(16, 9), dpi=100)
L = 250             # window size
ax1 = fig.add_subplot(121, xlim=(-L, L), ylim=(-L, L))
ax1.set_aspect('equal')
l = 5
ax2 = fig.add_subplot(122, xlim=(-l, l), ylim=(-l, l))
ax2.set_aspect('equal')
# object plot
P_s, = ax1.plot([], color='orange', marker='o', markersize=25)
P_v, = ax1.plot([], color='green', marker='.', markersize=10)
P_e, = ax1.plot([], color='blue', marker='.', markersize=10)
P_m, = ax1.plot([], color='black', marker='.', markersize=5)
ax1.legend(['Sun', 'Venus', 'Earth', 'Moon'], loc='upper left')
# trail plot
tr_s, = ax1.plot([], color='orange', alpha=0.3, lw=1)
tr_v, = ax1.plot([], color='green', alpha=0.3, lw=1)
tr_e, = ax1.plot([], color='cyan', alpha=0.5, lw=1)
tr_m, = ax1.plot([], color='black', alpha=0.3, lw=1)
time_text = ax1.text(L*0.60, L*0.90, '')

P_e2, = ax2.plot([], color='blue', marker='.', markersize=10)
P_m2, = ax2.plot([], color='black', marker='.', markersize=5)
tr_e2, = ax2.plot([], color='cyan', alpha=0.5, lw=1)
tr_m2, = ax2.plot([], color='black', alpha=0.3, lw=1)

lsx, lsy, lvx, lvy, lex, ley, lmx, lmy = [], [], [], [], [], [], [], []
dt = 0.005          # in program calculation delay time


def Track(o, perspective):
    (xx, yy) = (o.pos[0][0] - perspective.pos[0][0], o.pos[1][0] - perspective.pos[1][0])
    return xx, yy


perspective = moon
def animate(frame):
    (sx, sy) = Track(sun, perspective)
    (vx, vy) = Track(venus, perspective)
    (ex, ey) = Track(earth, perspective)
    (mx, my) = Track(moon, perspective)
    P_s.set_data((sx, sy))
    P_v.set_data((vx, vy))
    P_e.set_data((ex, ey))
    P_m.set_data(mx, my)
    P_e2.set_data((ex, ey))
    P_m2.set_data(mx, my)
    
    lsx.append(sx)
    lsy.append(sy)
    lvx.append(vx)
    lvy.append(vy)
    lex.append(ex)
    ley.append(ey)
    lmx.append(mx)
    lmy.append(my)
    time_text.set_text('time = %.1fdays' % (frame*365/4450))
    trail_length = 1500         # in frames
    tr_s.set_data(lsx[-trail_length:], lsy[-trail_length:])
    tr_v.set_data(lvx[-trail_length:], lvy[-trail_length:])
    tr_e.set_data(lex[-trail_length:], ley[-trail_length:])
    tr_m.set_data(lmx[-trail_length:], lmy[-trail_length:])
    tr_e2.set_data(lex[-trail_length:], ley[-trail_length:])
    tr_m2.set_data(lmx[-trail_length:], lmy[-trail_length:])

    sun.force = Net_F(sun, [venus, earth])
    venus.force = Net_F(venus, [sun, earth])
    earth.force = Net_F(earth, [sun, venus, moon])
    moon.force = Net_F(moon, [earth, sun])

    sun.momentum = sun.momentum + sun.force * dt
    venus.momentum = venus.momentum + venus.force * dt
    earth.momentum = earth.momentum + earth.force * dt
    moon.momentum = moon.momentum + moon.force * dt

    sun.pos = sun.pos + sun.momentum * dt / sun.mass
    venus.pos = venus.pos + venus.momentum * dt / venus.mass
    earth.pos = earth.pos + earth.momentum * dt / earth.mass
    moon.pos = moon.pos + moon.momentum*dt/moon.mass

    if frame % 300 == 0:				# for checking animation progress
        print(frame / 60, '%' )


ani = FuncAnimation(fig, animate, frames=6000, interval=10)
plt.suptitle('Perspective : '+ perspective.name+' (Approximated version)')
ax2.set_title('zoomed in earth-moon system')
ax1.grid()
ax2.grid()
print('Running...')
f_location = 'outputs/drunk_venus.mp4'
Writer = FFMpegWriter(fps=100)
ani.save(f_location, writer=Writer)
print('Completed')
plt.show()


# ideal values for approximation:
#Sun(mass=333000, pos=0, mom=0)
#Venus(mass=0.81, pos=107(108.9), mom=45.3)
#Earth(mass=1, pos=147.1(152), mom=48)
#Moon(mass=0.0123, pos.relative_to_earth=0.37(0.4), mom=0.06115)
#
# I need suitable data to make that kind of funny animation of drunk venus!!!

