# uniformity of random integer mumber generation in range(0,10):

import numpy as np
import matplotlib.pyplot as plt

lst = np.random.randint(0,10,size = 10000)

ss = []

for i in range(10):
    c = 0
    
    for j in range (len(lst)):
        if lst[j] == i:
            c = c + 1
            
    plt.bar(i,c,width= 0.25)
    ss.append('number of '+str(i)+'s: '+str(c))

plt.legend(ss,loc = 4)

plt.show()
