'''
DETERMINATION OF THE MEAN GRAPH USING LEAST SQUARE METHOD :

Author : Anik Mandal
'''

import matplotlib.pyplot as plt
import numpy as np

xx = np.array([-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
yy = np.array([-10.0, -7.0, -3.0, 2.0, 6.0, 8.0, 11.0, 13.0, 17.0, 22.0, 25.0])

(sumx, sumy, p1, p2) = (0.0, 0.0, 0.0, 0.0)

for k in range(len(xx)):
    sumx = sumx+xx[k]
    sumy = sumy+yy[k]

xb = sumx/len(xx)
yb = sumy/len(yy)

for l in range(len(xx)):
    p1 = p1+(xx[l]-xb)*(yy[l]-yb)
    p2 = p2+(xx[l]-xb)**2

m = p1/p2
c = yb-m*xb

xx1 = xx
yy1 = m*xx1+c

plt.plot(xx, yy, "*r", xx1, yy1, "-b")

plt.xlabel("x data ")
plt.ylabel("y data ")
plt.legend(["Experimental Data", "Mean Graph"])
plt.suptitle("DETERMINATION OF THE MEAN GRAPH USING LEAST SQUARE METHOD")
plt.title("xx="+str(xx)+"\nyy="+str(yy)+"\nCalculated slope of the graph :"+str(m)+" And intersect :"+str(c))
plt.grid()

plt.show()
