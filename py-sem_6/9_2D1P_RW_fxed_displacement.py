'''
2 Dim. 1 particle random walk: Fixed displacement 

Author : Anik Mandal
'''

import numpy as np
import matplotlib.pyplot as plt

conf_n = 1000
event_n = 1000
s_n = 16
avg_rms = 0

axis_conf = []
axis_rms = []
rr_list = []

for i in range(conf_n):
    sum_r2 = 0
    rr = []
    for j in range(event_n):
        sum_x, sum_y = 0, 0
        for k in range(s_n):
            th = np.random.uniform(0, 2 * np.pi)
            x = np.cos(th)
            y = np.sin(th)
            sum_x = sum_x + x
            sum_y = sum_y + y

        r2 = (sum_x**2 + sum_y**2)
        sum_r2 = sum_r2 + r2
        rr.append(r2**0.5)

    rms = (sum_r2/event_n)**0.5
    avg_rms = (avg_rms * i + rms)/(i + 1)

    axis_conf.append(i)
    axis_rms.append(avg_rms)
    rr_list.append(rr)

# RMS Fluctuation:
# plt.plot(axis_conf, axis_rms)
# plt.suptitle('2D 1 Particle Random walk-Displacement fixed\nRMS Fluctuation')
# plt.title('conf_n: ' + str(conf_n) + '; event_n: ' + str(event_n) + '; step_n: ' + str(s_n))
# plt.xlabel('Conf_n')
# plt.ylabel('Avg RMS value')

# Probability Density:
dis_x = np.array([i for i in range(s_n)])
prob = []

for i in range(len(dis_x)):
    count = 0
    for j in range(len(rr_list)):
        for k in range(len(rr_list[1])):
            if i <= rr_list[j][k] < (i+1):
                count = count + 1
    avg_count = count/len(rr_list)
    prob.append(avg_count/len(rr_list[1]))

plt.bar(dis_x, prob)
plt.suptitle('2D 1 Particle Random walk-Displacement fixed\nProbability density')
plt.title('conf_n: ' + str(conf_n) + '; event_n: ' + str(event_n) + '; step_n: ' + str(s_n))
plt.xlabel('Displacement window')
plt.ylabel('Probability of Occurrence')

plt.show()
