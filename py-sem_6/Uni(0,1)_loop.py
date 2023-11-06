# uniformity of random integer mumber generation in range(0,10):

import numpy as np
import matplotlib.pyplot as plt

ss = []
n = 20
l = 1000
r = 10000
count = np.zeros([l, n])

for i in range(l):
    lst = np.random.random(size=r)
    for j in range(n):
        c = 0
        for k in range(r):
            if j / n <= lst[k] < (j + 1) / n:
                c = c + 1
        count[i][j] = c

for i in range(n):
    s = 0
    for j in range(l):
        s = s + count[j][i]
    avgn = s / l
    plt.bar(i / n + 0.025, avgn, width=0.045)
    ss.append("avg_interval [" + str(i / n) + "," + str((i + 1) / n) + "]: " + str(avgn))

plt.title("Number of loops: " + str(l) + ", Number of random numbers in one loop: " + str(r))
plt.legend(ss, loc=4)
plt.show()
