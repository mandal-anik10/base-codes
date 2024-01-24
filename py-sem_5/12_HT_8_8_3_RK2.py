'''
#2: Solving ODE for a two label radioctive decay using RK-2

Author : Anik Mandal
'''

import numpy as np
import matplotlib.pyplot as plt
import json

t0 = 0
N = 0

l1 = 0.10
l2 = 0.08

h = 0.1
n = 401

t1 = t0
N1 = N
Nd = N

tt = [t0]
NN = [N]
zz = [0]


def m(t, N_2):
    s = l1*np.exp(-l1*t)-l2*N_2     # ODE
    return s


i = 0
while i < n-1:
    m1 = m(t1, Nd)
    Nd = Nd + h*m1
    t1 = t1 + h
    m2 = m(t1, Nd)

    N1 = N1 + h*(m1 + m2)/2

    tt.append(t1)
    NN.append(N1)

    z = (l1/(l1-l2))*(np.exp(-l2*t1)-np.exp(-l1*t1))
    zz.append(z)
    i = i+1

ig = np.trapz(NN, tt, dx=tt[1]-tt[0])
print('Value of Integration(0s to 40s)', ig)

t_data=[]
N_data=[]
for i in range (len(tt)):
    if round(tt[i],1)%1==0:
        t_data.append(tt[i])
        N_data.append(NN[i])

data = {'Time(s)': t_data, 'N_2': N_data}
with open('/home/anik/base-codes/py-sem_5/val_8_8_3.json', 'w') as f:
    json.dump(data, f)
print(data)


plt.plot(tt, NN, 'r')
plt.plot(tt, zz, '--c')

plt.xlim(-0.5, 40.5)
plt.xlabel('Time(s)')
plt.ylabel('N')
plt.legend(['Curve through RK2 method(h = 0.1)', 'Actual Curve'])
plt.grid()
plt.show()
