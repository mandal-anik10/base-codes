import numpy as np
import matplotlib.pyplot as plt
from LocalModule.Basic import *

event_n = 1000
loop_n = 1000


def Random_W(s_n):
    list_pn = []
    for i in range(loop_n):
        pp = []

        for j in range(event_n):
            step = np.random.randint(0, 2, size=s_n)
            cl = 0
            cr = 0

            for k in range(len(step)):
                if step[k] == 0:
                    cl = cl + 1
                else:
                    cr = cr + 1

            pos = cr - cl
            pp.append(pos)

        pn = []
        for m in range(-s_n, s_n+1):
            c = 0
            for n in range(len(pp)):
                if pp[n] == m:
                    c = c+1
            pn.append(c)

        list_pn.append(pn)
    xx = np.array([i for i in range(-s_n, s_n+1, 1)])
    avg_pn = []
    for i in range(len(list_pn[0])):
        total_pn = 0
        for j in range(len(list_pn)):
            total_pn = total_pn + list_pn[j][i]
        avg_pn.append(total_pn/len(list_pn))

    avg_pn = np.array(avg_pn)
    avg_pos = Sum(xx*avg_pn)/Sum(avg_pn)
    rms2_pos = (Sum(((xx**2)*avg_pn))/Sum(avg_pn))
    return [xx, avg_pn, avg_pos, rms2_pos]


conf = [i for i in range(10, 20)]
ideal_rms2 = np.array(conf)
list_rms2 = []
for i in range(len(conf)):
    rms2_val = Random_W(conf[i])[3]
    list_rms2.append(rms2_val)

plt.plot(conf, list_rms2, conf, ideal_rms2, '.r')

plt.suptitle("1D 1 particle random walk")
t = "Mean square of distance against step_n\n"+"Loop_n: "+str(loop_n)+", Event_n per loop: "+str(event_n)
plt.title(t)
plt.legend(["Simulated output", "Theoretical output"])
plt.xlabel("Step_n taken")
plt.ylabel("Avg RMS distance$^2$(Mean square of distance)")
plt.grid()
plt.show()
