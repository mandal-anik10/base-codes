'''
JEST 2024: question - 1 (Part : A)
Motion of test charges (positive and negative) due to three stationary
charges placed at the corners of an equilateral triangle.

Author : Anik Mandal
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from utils import *
import tqdm
import warnings
warnings.filterwarnings('ignore')

class Charge:
    # A Charge class to define parameters of point charge
    def __init__(self, mass, charge, pos, momentum, force=[[0],[0], [0]]):
        self.mass = mass
        self.charge = charge
        self.pos = pos
        self.momentum = momentum
        self.force = force


def Coulomb_F(on_o, due_to_o):
    # Law that governs the system
    # on_o : force on the object
    # due_to_o : force due to the object
    K = 1           # 1/4*\pi*\epsilon_0
    r_vec = V_Sum(on_o.pos, V_Neg(due_to_o.pos))
    r_mag = V_Mod(r_vec)
    r_cap = r_vec/r_mag
    f_mag = K * on_o.charge * due_to_o.charge / r_mag ** 2
    f_vec = f_mag*r_cap
    return f_vec


def Net_F(on_o, o):
    # calculating net force vector on the chrges
    # on_o : on the object
    # o : due to the object

    s = 0
    for i in range(len(o)):
        s = s + Coulomb_F(on_o, o[i])
    return s

# Defining 3 stationary charges at 3 cornors of 
C_1 = Charge(mass=1, charge=1,  pos=[[1], [0], [0]], momentum=[[0], [0], [0]])
C_2 = Charge(mass=1, charge=1,  pos=[[np.cos(np.deg2rad(120))], [np.sin(np.deg2rad(120))], [0]], momentum=[[0], [0], [0]])
C_3 = Charge(mass=1, charge=1,  pos=[[np.cos(np.deg2rad(240))], [np.sin(np.deg2rad(240))], [0]], momentum=[[0], [0], [0]])

# initial perturbation as added momentum
# mean_m = 0
# sd_m = 1
# np.random.seed(123456789)
# ini_m = [[np.random.normal(mean_m, sd_m)], [np.random.normal(mean_m, sd_m)], [0]]   
ini_m = [[0], [1.5], [0]]

# defining test charges
TC_pos = Charge(mass=1, charge=1, pos=[[0], [0], [0]], momentum=ini_m)
TC_neg = Charge(mass=1, charge=-1, pos=[[0], [0], [0]], momentum=ini_m)

# plotting:
fig = plt.figure(figsize=(16, 9), dpi=100)
L = 5
# ax1 for positive charge
ax1 = fig.add_subplot(121, xlim=(-L, L), ylim=(-L, L))
ax1.set_aspect('equal')
# ax2 for negative charge
ax2 = fig.add_subplot(122, xlim=(-L, L), ylim=(-L, L))
ax2.set_aspect('equal')

# setting plot objects 
P_c11, = ax1.plot([], color='red', marker='o', markersize=5)
P_c21, = ax1.plot([], color='red', marker='o', markersize=5)
P_c31, = ax1.plot([], color='red', marker='o', markersize=5)
P_tp, = ax1.plot([], color='red', marker='o', markersize=5)
tr_tp, = ax1.plot([], color='red', alpha=0.3, lw=1)
time_text = ax2.text(L*0.70, L*0.90, '')

P_c12, = ax2.plot([], color='red', marker='o', markersize=5)
P_c22, = ax2.plot([], color='red', marker='o', markersize=5)
P_c32, = ax2.plot([], color='red', marker='o', markersize=5)
P_tn, = ax2.plot([], color='blue', marker='o', markersize=5)
tr_tn, = ax2.plot([], color='blue', alpha=0.3, lw=1)


lTpx, lTpy, lTnx, lTny =[], [], [], []      # to store trail data
# increment in time per frame
dt = 0.0015
progress = tqdm.tqdm(total=6000, desc='Frames collected')

def animate(frame):
    # main function that does everything in each frame

    # setting plot axes lengths
    if abs(TC_pos.pos[0][0]) > 4.5 or abs(TC_pos.pos[1][0]) > 4.5:
        Lp = np.max([abs(TC_pos.pos[0][0]), abs(TC_pos.pos[1][0])])
        ax1.set_xlim([-Lp*10/9, Lp*10/9])
        ax1.set_ylim([-Lp*10/9, Lp*10/9])
    if abs(TC_neg.pos[0][0]) > 4.5 or abs(TC_neg.pos[1][0]) > 4.5:
        Ln = np.max([abs(TC_neg.pos[0][0]), abs(TC_neg.pos[1][0])])
        ax2.set_xlim([-Ln*10/9, Ln*10/9])
        ax2.set_ylim([-Ln*10/9, Ln*10/9])

    # setting data to plot objects
    (C1x, C1y) = (C_1.pos[0][0], C_1.pos[1][0])     # position of charge-1 in each frame
    (C2x, C2y) = (C_2.pos[0][0], C_2.pos[1][0])     # position of charge-2 in each frame
    (C3x, C3y) = (C_3.pos[0][0], C_3.pos[1][0])     # position of charge-3 in each frame

    (Tpx, Tpy) = (TC_pos.pos[0][0], TC_pos.pos[1][0])   # position of test-charge positive in each frame
    (Tnx, Tny) = (TC_neg.pos[0][0], TC_neg.pos[1][0])   # position of test-charge negative in each frame
    P_c11.set_data((C1x, C1y))
    P_c21.set_data((C2x, C2y))
    P_c31.set_data((C3x, C3y))
    P_c12.set_data((C1x, C1y))
    P_c22.set_data((C2x, C2y))
    P_c32.set_data((C3x, C3y))

    P_tp.set_data(Tpx, Tpy)
    P_tn.set_data(Tnx, Tny)

    # creating charge path trails
    lTpx.append(Tpx)
    lTpy.append(Tpy)
    lTnx.append(Tnx)
    lTny.append(Tny)
    time_text.set_text('time = %.1fs' % (frame * dt))
    trail_length = 4000  # in frames
    tr_tp.set_data(lTpx[-trail_length:], lTpy[-trail_length:])
    tr_tn.set_data(lTnx[-trail_length:], lTny[-trail_length:])

    # force on the test charges in each frame
    TC_pos.force = Net_F(TC_pos, [C_1, C_2, C_3])
    TC_neg.force = Net_F(TC_neg, [C_1, C_2, C_3])

    # momentum of the test charges in each frame
    TC_pos.momentum = TC_pos.momentum + TC_pos.force * dt
    TC_neg.momentum = TC_neg.momentum + TC_neg.force * dt
    
    # position of the test charges in each frame
    TC_pos.pos = TC_pos.pos + TC_pos.momentum * dt / TC_pos.mass
    TC_neg.pos = TC_neg.pos + TC_neg.momentum * dt / TC_neg.mass

    # updating progress bar
    progress.update(1)

ax1.grid()
ax1.set_title('Red: Positive charge')
ax2.grid()
ax2.set_title('Blue: Negative charge')

# creating animaion
anim = FuncAnimation(fig, animate, frames=6000, interval=10)

print('Running...')
# saving animation as video file
f_location = 'outputs/jest24q1_test_charge_motion.mp4'
Writer = FFMpegWriter(fps=100)
anim.save(f_location, writer=Writer)
print('Completed')
plt.show()