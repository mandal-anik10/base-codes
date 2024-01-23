'''
Determination of the value of 0^0

Author : Anik Mandal
'''

import matplotlib.pyplot as plt
import numpy as np

x1=np.linspace(1,0.1,100)
x2=np.linspace(0.1,0.01,30)
x3=np.linspace(0.01,0.001,20)
x4=np.linspace(0.001,0.00001,50)

y1=x1**x1
y2=x2**x2
y3=x3**x3
y4=x4**x4

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
plt.plot(x4,y4)

plt.title("lim(a―>0) a^a : Determination of the value of 0^0")
plt.xlabel("a")
plt.ylabel("a^a")
plt.grid()
plt.show()