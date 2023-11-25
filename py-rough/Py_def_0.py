import numpy as np
import matplotlib.pyplot as plt
from LocalModule.Curve_FIt import Linear_Fit
g = 100000
xx = []
yy = []
for i in range(313):
    x = np.log10(g)
    xx.append(-x)
    s = 1

    p = g+s
    while p > g:
        s = s/10
        p = g+s
    y = np.log10(s)
    yy.append(-y)
    print(x, y)
    g = g / 10

m, c = Linear_Fit(xx, yy)
x = np.linspace(0,300,301)
y = m*x+c
# plt.plot(x,y)
plt.plot(xx, yy)
plt.title('Minimum value of s after which it will consider p = g + s as g')
plt.legend(['slope:'+str(m)+'   intersect:'+str(c)])
plt.xlabel('$x = -log_{10}(g)$')
plt.ylabel('$y = -log_{10}(s)$')
plt.grid()
plt.show()