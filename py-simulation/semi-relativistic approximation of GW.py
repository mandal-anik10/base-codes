import numpy as np
from matplotlib.animation import FuncAnimation, FFMpegFileWriter
import matplotlib.pyplot as plt
from LocalModule.Vector_Operation import *

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(121)
ax1.set_aspect('equal')
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)

ax2 = fig.add_subplot(122)
ax2.set_aspect('equal')
fig.tight_layout()


# Defined constants:
k = 1



class BH:
    def __init__(self,id, mass, pos, momentum, force=None):
        self.id = id
        self.mass = mass
        self.pos = pos
        self.momentum = momentum
        self.force = force


# def Grav_F(on_o, due_to_o):
#     G = 1
#     r_vec = V_Sum(on_o.pos, V_Neg(due_to_o.pos, 3), 3)
#     r_mag = V_Mod(r_vec, 3)
#     r_cap = r_vec/r_mag
#     f_mag = -G * on_o.mass * due_to_o.mass / r_mag ** 2
#     f_vec = f_mag*r_cap
#     return f_vec


# def Net_F(on_o, o):
#     s = 0
#     for i in range(len(o)):
#         s = s + Grav_F(on_o, o[i])
#     return s

BH1 = BH(id = 1, mass=1, pos= [[-1], [0]], momentum=[[1], [0]])

BH1.mass
def Potential_Field(loc_vector, object):
    r = V_Subtract(loc_vector, object.pos, 2)
    v = k * object.mass/V_Mod(r,2)
    return v

eps = 0.01

x_cord = np.linspace(-5, 5, 100)
y_cord = np.linspace(-5, 5, 100)
Px, Py = [], []


for i in range(len(x_cord)):
    if abs(x_cord[i]) > eps :
        Px.append(x_cord[i])
for j in range(len(y_cord)):
    if abs(y_cord[j]) > eps:
        Py.append(y_cord)

V_p = []


for i in range(len(Px)):
    vp = []
    for j in range(len(Py)):
        point = [[Px[i]], [Py[j]]]
        print(point)
        v = Potential_Field(point, BH1)
        vp.append(v)

    V_p.append(vp)

# def animate(frame):
#     ax1.plot([BH1.pos[0][0]],[BH1.pos[1][0]], '.k' )

#     BH1.pos = BH1.pos + V_Scale(1/(100*BH1.mass), BH1.momentum, 2)


    
            
ax1.plot([BH1.pos[0][0]],[BH1.pos[1][0]], '.k' )


# ax2.imshow(V_p, cmap='inferno')

# ani =  FuncAnimation(fig, animate, frames= 1200, interval = 50)


plt.show()
