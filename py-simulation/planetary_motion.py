'''
Simulating planetary motion of sun-earth-moon system

Author : Anik Mandal
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from utils import *

class Object:
    def __init__(self, mass, pos, momentum, force=None):
        self.mass = mass
        self.pos = pos
        self.momentum = momentum
        self.force = force

def Grav_F(on_o,due_to_o):
    G = 1
    r_vec = V_Sum(on_o.pos,V_Neg(due_to_o.pos))
    r_mag = V_Mod(r_vec)
    r_cap = r_vec/r_mag
    f_mag = -G*(on_o.mass)*(due_to_o.mass)/r_mag**2
    f_vec = f_mag*r_cap
    return f_vec

# star:
star = Object(mass=333000,
              pos=[[0], [0], [0]],
              momentum=[[0], [0], [0]])
# planet:
earth = Object(mass=1,
               pos=[[147.1], [0], [0]],
               momentum=[[0],[48], [0]])
venus = Object(mass=0.81,
               pos=[[107.0], [0], [0]],
               momentum=[[0], [45.3], [0]])
# sub_planet:
# moon = Object(mass=0.012,
#               pos=[[159.5],[0],[0]],
#               momentum=[[0],[0.5],[0]])

fig = plt.figure(figsize=(16,9), dpi=100)
L =200
ax = fig.add_subplot(xlim = (-L, L), ylim = (-L, L))
ax.set_aspect('equal')

p_S = ax.plot([], color='orange', marker='o')
p_P1 = ax.plot([], color='blue', marker='o')
p_P2 = ax.plot([], color='green', marker='o')
# p_m = ax.plot([], color='gray', marker='.')

lines, = ax.plot([], color='orange', alpha=0.3, lw=1)
line1, = ax.plot([], color='blue', alpha=0.3, lw=1)
line2, = ax.plot([], color='green', alpha=0.3, lw=1)
# linem, = ax.plot([], color='gray', alpha=0.3, lw=1)

time_text = ax.text(L*0.70, L*0.90,'')

lsx,lsy, l1x, l1y, l2x, l2y, lmx, lmy =[], [], [], [], [], [], [], []
dt = 0.025
def animate(frame):
    (sx, sy) = (star.pos[0][0], star.pos[1][0])
    (p1x, p1y) = (earth.pos[0][0], earth.pos[1][0])
    (p2x, p2y) = (venus.pos[0][0], venus.pos[1][0])
    # (pmx, pmy) = (moon.pos[0][0], moon.pos[1][0])
    p_S[0].set_data((sx, sy))
    p_P1[0].set_data((p1x, p1y))
    p_P2[0].set_data((p2x, p2y))
    # p_m[0].set_data(pmx, pmy)

    lsx.append(sx)
    lsy.append(sy)
    l1x.append(p1x)
    l1y.append(p1y)
    l2x.append(p2x)
    l2y.append(p2y)
    # lmx.append(pmx)
    # lmy.append(pmy)
    time_text.set_text('time = %.1fs' % (frame*dt))
    trail_length = 700         #in frames
    lines.set_data(lsx[-trail_length:], lsy[-trail_length:])
    line1.set_data(l1x[-trail_length:], l1y[-trail_length:])
    line2.set_data(l2x[-trail_length:], l2y[-trail_length:])
    # linem.set_data(lmx[-trail_length:], lmy[-trail_length:])


    s_force = Grav_F(star, earth)+Grav_F(star, venus)
    p1_force = Grav_F(earth, star)+Grav_F(earth, venus)
    p2_force = Grav_F(venus, star)+Grav_F(venus, earth)
    # m_force = Grav_F(moon, earth)

    star.momentum = star.momentum + s_force*dt
    earth.momentum = earth.momentum + p1_force*dt
    venus.momentum = venus.momentum + p2_force*dt
    # moon.momentum = moon.momentum + m_force*dt

    star.pos = star.pos + star.momentum*dt/star.mass - star.pos
    earth.pos = earth.pos + earth.momentum*dt/earth.mass - star.pos
    venus.pos = venus.pos + venus.momentum*dt/venus.mass - star.pos
    # moon.pos = moon.pos + moon.momentum*dt/moon.mass - star.pos

    if frame % 300 == 0:				# for checking animation progress
        print(frame / 60, '%' )


ani = FuncAnimation(fig, animate, frames=6000, interval=25)

print('Running...')
f_location = 'outputs/planetary_motion.mp4'
Writer = FFMpegWriter(fps=40)
ani.save(f_location, writer=Writer)
print('Completed')
plt.grid()
plt.show()