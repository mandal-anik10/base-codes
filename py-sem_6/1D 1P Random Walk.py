# 1 Dim. 1 particle random walk:

import numpy as np
import matplotlib.pyplot as plt
# from LocalModule.Basic import Sum       # Local module, you can define a function Sum which will add elements of a
# list


def Sum(num_list):
    s = 0
    for i in range(0, len(num_list)):
        s = s + num_list[i]
    return s


s_n = 16                # step number
event_n = 1000          # event number
loop_n = 1000           # loop number

list_pn = []            # list of for pn of all loops
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

    list_pn.append(pn)

final_s = np.array([i for i in range(-s_n, s_n+1, 1)])      # final step
avg_pn = []                             # to store avg value of all numbers per position(pn s)

for i in range(len(list_pn[0])):
    total_pn = 0
    for j in range(len(list_pn)):
        total_pn = total_pn + list_pn[j][i]
    avg_pn.append(total_pn/len(list_pn))

avg_pn = np.array(avg_pn)
prob_pn = avg_pn/Sum(avg_pn)

# statistical calculation:
avg_pos = Sum(final_s*avg_pn)/Sum(avg_pn)
rms_pos = (Sum(((final_s**2)*avg_pn))/Sum(avg_pn))**0.5

# plt.bar(final_s, avg_pn)
plt.bar(final_s, prob_pn)

plt.suptitle("1D 1 particle random walk")
t = "Loop_n: "+str(loop_n)+", Event_n per loop: "+str(event_n)+", Steps_n per event: "+str(s_n)
r = "After entire event\nAvg position: "+str(avg_pos)+",\nRMS position: "+str(rms_pos)
plt.title(t)
a = plt.text(7, 175, r)
plt.xlabel("Position after "+str(s_n)+" random steps")
plt.ylabel("Avg probability of happening")

plt.show()
