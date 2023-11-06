
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from LocalModule.Vector_Operation import *


class Object:
    def __init__(self, mass, pos, momentum, force=None):
        self.mass = mass
        self.pos = pos
        self.momentum = momentum
        self.force = force


def Grav_F(on_o, due_to_o):
    G = 1
    r_vec = V_Sum(on_o.pos, V_Neg(due_to_o.pos, 3), 3)
    r_mag = V_Mod(r_vec, 3)
    r_cap = r_vec/r_mag
    f_mag = -G * on_o.mass * due_to_o.mass / r_mag ** 2
    f_vec = f_mag*r_cap
    return f_vec


def Net_F(on_o, o):
    s = 0
    for i in range(len(o)):
        s = s + Grav_F(on_o, o[i])
    return s


earth = Object(mass=100, pos=[[0], [0], [0]], momentum=[[0], [0], [0]])
moon = Object(mass=2, pos=[[1], [0], [0]], momentum=[[0], [5], [0]])

# plotting:
fig = plt.figure(figsize=(16, 9), dpi=100)
L = 5
ax = fig.add_subplot(xlim=(-L, L), ylim=(-L, L))
ax.set_aspect('equal')

P_e, = ax.plot([], color='blue', marker='o', markersize=1)
P_m, = ax.plot([], color='black', marker='.', markersize=0.5)

tr_e, = ax.plot([], color='blue', alpha=0.3, lw=1)
tr_m, = ax.plot([], color='black', alpha=0.3, lw=1)
time_text = ax.text(L*0.70, L*0.90, '')

lex, ley, lmx, lmy =[], [], [], []
dt = 0.025


def Track(o, perspective):
    (xx, yy) = (o.pos[0][0] - perspective.pos[0][0], o.pos[1][0] - perspective.pos[1][0])
    return xx, yy


perspective = earth


def animate(frame):
    (ex, ey) = Track(earth, earth)
    (mx, my) = Track(moon, earth)
    P_e.set_data((ex, ey))
    P_m.set_data(mx, my)

    lex.append(ex)
    ley.append(ey)
    lmx.append(mx)
    lmy.append(my)
    time_text.set_text('time = %.1fs' % (frame * dt))
    trail_length = 400  # in frames
    tr_e.set_data(lex[-trail_length:], ley[-trail_length:])
    tr_m.set_data(lmx[-trail_length:], lmy[-trail_length:])

    earth.force = Net_F(earth, [moon])
    moon.force = Net_F(moon, [earth])

    earth.momentum = earth.momentum + earth.force * dt
    moon.momentum = moon.momentum + moon.force * dt

    earth.pos = earth.pos + earth.momentum * dt / earth.mass
    moon.pos = moon.pos + moon.momentum * dt / moon.mass


anim = FuncAnimation(fig, animate, frames=1200, interval=25)

print('Running...')
f_location = r'C:\Users\Anik Mandal\Videos\PY3 Videos\Two Body Motion.mp4'
Writer = FFMpegWriter(fps=40)
# anim.save(f_location, writer=Writer)
print('Completed')
plt.grid()
plt.show()