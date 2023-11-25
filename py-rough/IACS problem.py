# Equal charges 'q' located at the four vertices of a square.
# The number of neutral points of this charge distribution is
# [4, 5, 1, 6] ; my answer=1, answer given = 5

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# let, q = 1 and k = 1/4.pi.\epsillon_0 = 1

xx = []
yy = []
for i in range(1000):
    for j in range(1000):
        x = -1 + i*0.002
        y = -1 + j*0.002
        xx.append(x)
        yy.append(y)


def unit_v(rx, ry):
    r = (rx**2+ry**2)**0.5
    unit = [rx/r, ry/r]
    return unit


def field(charge_locx, charge_locy):
    elec_fmag = []
    for i in range(len(xx)):
        rx = xx[i]-charge_locx
        ry = yy[i]-charge_locy
        ur = unit_v(rx, ry)
        r_mag2 = rx**2+ry**2
        f_mag = 1/r_mag2
        f_vec = [ur[0]*f_mag, ur[1]*f_mag]
        elec_fmag.append(f_vec)
    return elec_fmag


Q1f = field(np.pi/5, np.pi/5)
Q2f = field(-np.pi/5, np.pi/5)
Q3f = field(-np.pi/5, -np.pi/5)
Q4f = field(np.pi/5, -np.pi/5)
zz = []

for i in range(len(Q1f)):
    total_fx = Q1f[i][0]+Q2f[i][0]+Q3f[i][0]+Q4f[i][0]
    total_fy = Q1f[i][1]+Q2f[i][1]+Q3f[i][1]+Q4f[i][1]
    total_f = [total_fx, total_fy]
    zz.append((total_fx**2+total_fy**2)**0.5)

ax.plot(xx, yy, zz, '.')
ax.set_zlim([0, 10])
plt.show()

