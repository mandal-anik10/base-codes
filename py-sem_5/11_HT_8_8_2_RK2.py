'''
#1: Solving ODE for a particle free falling in air using RK-2

Author : Anik Mandal
'''

import numpy as np
import matplotlib.pyplot as plt
import json

t0 = 0
v0 = 0

g = 9.80
a = 0.2

h = 0.1
n = 2001

t1 = t0
v1 = v0
vd = v0

tt = [t0]
vv = [v0]
zz = [0]


def m(t, v):
    s = g-a*v           # ODE
    return s


i = 0
while i < n-1:
    m1 = m(t1, vd)
    vd = vd + h*m1
    t1 = t1 + h
    m2 = m(t1, vd)

    v1 = v1 + h*(m1 + m2)/2

    tt.append(t1)
    vv.append(v1)

    z = (g/a)*(1-np.exp(-a*t1))
    zz.append(z)
    i = i+1

ig = np.trapz(vv, tt, dx=tt[1]-tt[0])
print('Value of Integration(0s to 20s)', ig)
print('v(', t0+100*h, '):', vv[100])

t_data = []
v_data = []

for i in range(201):
    if round(tt[i],1)%1 == 0:
        t_data.append(tt[i])
        v_data.append(vv[i])

data = {'Time(s)': t_data, 'Velocity(m/s)': v_data}
with open('/home/anik/base-codes/py-sem_5/val_8_8_2.json', 'w') as f:
    json.dump(data, f)
print(data)

# let assume, v(inf)==v(200)
print('v(', t0+200*h, ')/v(inf):', vv[200]/vv[2000])

plt.plot(tt, vv, 'r', tt, zz, '--c')

plt.xlim(-0.5, 20.5)
plt.legend(['Curve through RK2 method', 'Actual Curve'])
plt.xlabel("time(s)")
plt.ylabel(r"velocity($ms^{-1}$)")
plt.grid()
plt.show()
