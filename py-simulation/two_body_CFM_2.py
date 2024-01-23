'''
Simulating central force motion of two masses in two force regime

Author : Anik Mandal
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from utils import *

class Object:
    def __init__(self, name, mass, pos, momentum, force=None):
        self.name = name
        self.mass = mass
        self.pos = pos
        self.momentum = momentum
        self.force = force
        

def Force_F(on_o, due_to_o):
    r_vec = V_Sum(on_o.pos, V_Neg(due_to_o.pos))
    r_mag = V_Mod(r_vec)
    r_cap = r_vec/r_mag
    f_mag = -on_o.mass * due_to_o.mass / r_mag**2 + on_o.mass * due_to_o.mass / (r_mag)**3
    f_vec = f_mag*r_cap
    return f_vec


def Net_F(on_o, o):
    s = 0
    for i in range(len(o)):
        s = s + Force_F(on_o, o[i])
    return s


orange = Object(name='Orange', mass=10, pos=[[0], [0], [0]], momentum=[[0], [-0.5], [0]])
blue = Object(name='Blue', mass=2, pos=[[1.5], [0], [0]], momentum=[[0], [0.5], [0]])

# plotting:

fig = plt.figure(figsize=(16, 9), dpi=100)
L = 2
ax = fig.add_subplot(xlim=(-L, L), ylim=(-L, L))
ax.set_aspect('equal')


P_e, = ax.plot([], color='orange', marker='o')
P_m, = ax.plot([], color='blue', marker='o')
# fieldp, = ax.plot([], color='orange', alpha=0.1, marker='o', markersize=175)

tr_e, = ax.plot([], color='orange', alpha=0.3, lw=1)
tr_m, = ax.plot([], color='cyan', alpha=0.3, lw=1)
time_text = ax.text(L*0.70, L*0.90, '')

lex, ley, lmx, lmy =[], [], [], []
dt = 0.01


def potential_F(x, y):
    r = (x**2 + y**2)**0.5
    v = -1/r**2 + 1/r**3
    return v
x = y = np.linspace(-2, 2, 100)
x, y = np.meshgrid(x, y)
def Track(o, perspective):
    (xx, yy) = (o.pos[0][0] - perspective.pos[0][0], o.pos[1][0] - perspective.pos[1][0])
    return xx, yy


def CoM(o):
    p = [[0], [0], [0]]
    mx, my, mz, m = 0, 0, 0, 0
    for i in range(len(o)):
        mx = mx + o[i].pos[0][0] * o[i].mass
        my = my + o[i].pos[1][0] * o[i].mass
        mz = mz + o[i].pos[2][0] * o[i].mass
        m = m + o[i].mass
    p[0][0] = mx/m
    p[1][0] = my/m
    p[2][0] = mz/m
    return p


Center_M = Object(name='Center of Mass', mass=0, pos=CoM([orange, blue]), momentum=0)
perspective = orange


def animate(frame):
    (ex, ey) = Track(orange, perspective)
    (mx, my) = Track(blue, perspective)
    P_e.set_data((ex, ey))
    P_m.set_data(mx, my)
    # fieldp.set_data((ex, ey))
    plt.contour(potential_F(x, y))

    lex.append(ex)
    ley.append(ey)
    lmx.append(mx)
    lmy.append(my)
    time_text.set_text('time = %.1fs' % (frame * 0.01))
    trail_length = 1500  # in frames
    tr_e.set_data(lex[-trail_length:], ley[-trail_length:])
    tr_m.set_data(lmx[-trail_length:], lmy[-trail_length:])

    orange.force = Net_F(orange, [blue])
    blue.force = Net_F(blue, [orange])

    orange.momentum = orange.momentum + orange.force * dt
    blue.momentum = blue.momentum + blue.force * dt

    orange.pos = orange.pos + orange.momentum * dt / orange.mass
    blue.pos = blue.pos + blue.momentum * dt / blue.mass

    if frame%300 == 0:
        print(frame/60, '%')
    
    
ani = FuncAnimation(fig, animate, frames=6000, interval=10)
plt.title('Perspective : '+perspective.name)
print('Running...')
f_location = 'outputs/two_body_CFM_twoForceField.mp4'
Writer = FFMpegWriter(fps=100)
ani.save(f_location, writer=Writer)
print('Completed')
plt.grid()
plt.show()
