
# PLOTTING OF THE DIFFERENTIAL EQUATION OF A CRITICALLY DAMPED HARMONIC OSCILLATOR WITH BOUNDARY CONDITIONS :


import matplotlib.pyplot as plt
import numpy as np

# BOUNDARY CONDITIONS :
x = 0
y = 1
a = 1
b = -10

w = np.pi/2
g = 2*w

xx = []
yy = []

n = 500000
xs = 0.00001
i = 1

while i <= n:
    xx.append(x)
    yy.append(y)

    # SLOPE OF THE GRAPH AT BOUNDARY CONDITION:
    m = np.exp(-0.5*g*x)*(-0.5*g*(a+x*b)+b)

    c = y - m*x
    x = x + xs
    y = m*x + c

    i = i+1

xx = np.array(xx)
yy = np.array(yy)

plt.plot(xx, yy, 'r')

plt.suptitle("PLOTTING OF THE DIFFERENTIAL EQUATION OF A CRITICALLY DAMPED HARMONIC OSCILLATOR WITH BOUNDARY CONDITIONS")
plt.title("Damping constant 'g' :"+str(g)+"  And Actual angular frequency 'w' :"+str(w))
plt.xlabel("x values        x axis --->")
plt.ylabel("f(x) values        y axis --->")
plt.legend(["$y''  = -w^2y -gy'$\n$g =2w$"], loc="upper right")
plt.grid()

plt.show()
