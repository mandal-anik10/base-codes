'''
Simulating Toss of a Coin: Dstribution of number of heads for n tosses

Author : Anik Mandal
'''

import numpy as np
import matplotlib.pyplot as plt

ss = []

loop_n = 10000
toss_n = 20
event_n = 2**10

count = np.zeros([loop_n, toss_n + 1])

for i in range(loop_n):
    c_H = []
    for j in range(event_n):
        toss = np.random.randint(0, 2, size=toss_n)                # 0 as tail and 1 as head
        c = 0
        for p in range(len(toss)):
            if toss[p] == 1:
                c = c + 1
        c_H.append(c)

    for m in range(toss_n+1):
        for n in range(len(c_H)):
            if c_H[n] == m:
                count[i][m] = count[i][m] +1

for i in range(toss_n+1):
    s = 0
    for j in range(loop_n):
        s  = s + count[j][i]
    avgn = s/loop_n
    plt.bar(i, avgn, width=0.5)
    ss.append("avg_exp_n:"+str(avgn)+" with"+str(i)+" head")

t1 = "Loop_Number: "+str(loop_n)
t2 = ", Event_number per loop: $2^{"+str(toss_n/2)
t3 = "}$,\nToss_number per event: "+str(toss_n)

plt.title(t1+t2+t3)
plt.legend(ss)
plt.xlabel("Head number")
plt.ylabel("Event number")
plt.show()
