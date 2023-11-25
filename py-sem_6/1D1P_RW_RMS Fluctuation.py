# 1 Dim. 1 particle random walk:

import numpy as np
import matplotlib.pyplot as plt
from LocalModule.Basic import Sum

s_n = 16                # step number
event_n = 1000          # event number
loop_n = 10000           # loop number

list_pn = []            # list of for pn of all loops
avg_pos, rms_pos = 0, 0
conf, RMS = [], []
for i in range(loop_n):
    pp = []             # to store outcome position of all events

    for j in range(event_n):
        step = np.random.randint(0, 2, size=s_n)
        cl = 0
        cr = 0

        for k in range(len(step)):
            if step[k] == 0:
                cl = cl + 1
            else:
                cr = cr + 1

        pos = cr - cl               # position after an event
        pp.append(pos)

    pn = []                         # to store number of times a position achieved
    for m in range(-s_n, s_n+1):
        c = 0
        for n in range(len(pp)):
            if pp[n] == m:
                c = c+1
        pn.append(c)

    pn = np.array(pn)
    final_pos = np.array([i for i in range(-s_n, s_n + 1)])

    avg_pos = (avg_pos * i + Sum(final_pos*pn)/Sum(pn))/(i+1)
    rms_pos = (rms_pos * i + (Sum((final_pos**2)*pn)/Sum(pn))**0.5)/(i+1)

    RMS.append(rms_pos)
    conf.append(i+1)

    list_pn.append(pn)

# final_pos = np.array([i for i in range(-s_n, s_n+1)])

# for i in range(1,len(list_pn)+1):
#     avg_pos = 0
#     rms_pos = 0
#     for j in range(i):
#
plt.plot(conf, RMS)

plt.suptitle("1D 1 particle random walk")
t = "Loop_n: "+str(loop_n)+", Event_n per loop: "+str(event_n)+", Steps_n per event: "+str(s_n)
plt.title("RMS value against Configuration number(Fluctuation in RMS value) \n"+t)
plt.xlabel("Configuration Number")
plt.ylabel("RMS position")

plt.show()
