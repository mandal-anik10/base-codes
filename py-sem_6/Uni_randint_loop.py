# uniformity of random integer mumber generation in range(0,10):

import numpy as np
import matplotlib.pyplot as plt

ss = []
n = 10
l = 1000
r = 10000
count = np.zeros([l, n])

for i in range(l):
    lst = np.random.randint(0, 10, size=r)
    for j in range(n):
        c = 0
        for k in range(len(lst)):
            if lst[k] == j:
                c = c + 1
        count[i][j] = c

for i in range(n):
    s = 0
    for j in range(l):
        s = s + count[j][i]
    avg = s / l

    plt.bar(i, avg, width=0.25)
    ss.append('avg number of ' + str(i) + 's: ' + str(avg))

plt.title("number of loops: " + str(l) + ";number of random numbers in one loop: " + str(r))
plt.legend(ss, loc=4)

plt.show()
