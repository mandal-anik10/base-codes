'''
DETERMINATION OF THE BAR GRAPH OF THE NUMBER OF POINTS IN EACH WINDOWS THROUGH RANDOM NUMBER GENERATION :

Author : Anik Mandal
'''

import random as rd
import matplotlib.pyplot as plt

n = 1000000

a = 0
xx = []
cc = []
aa = []
ss = []

for i in range(n):
    x = rd.random()
    xx.append(x)

while a < 0.9:
    c = 0
    for i in range(n):
        if (xx[i] > a) & (xx[i] < (a+0.1)):
            c += 1
    cc.append(c)
    s = "$Points No.:$" + str(c)
    ss.append(s)

    a += 0.1
    aa.append(a)

for i in range(len(aa)):
    plt.bar(aa[i], cc[i], width=0.1)

plt.suptitle("DETERMINATION OF THE BAR GRAPH OF THE NUMBER OF POINTS IN EACH WINDOWS THROUGH RANDOM NUMBER GENERATION ")
plt.title("Total numbers of points : "+str(n))
plt.legend(ss)
plt.ylabel("Value of the number in partitions")
plt.xlabel("Number of points")
plt.xlim(0, 1.3)
plt.show()
