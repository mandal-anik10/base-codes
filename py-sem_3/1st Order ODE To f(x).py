
# PLOTTING OF THE FUNCTION THROUGH IT'S 1ST ORDER DIFFERENTIAL EQUATION AND BOUNDARY CONDITIONS :


import matplotlib.pyplot as plt
import numpy as np

# BOUNDARY CONDITIONS :
x = 0.0
y = 0.0

xx = []
yy = []


n = 500000
xs = 0.00001

i = 1

while i <= n:
    xx.append(x)
    yy.append(y)

    # SLOPE OF THE GRAPH AT BOUNDARY CONDITION:
    m = np.sin(x)-2*y

    c = y - m*x
    x = x + xs
    y = m*x + c

    i = i+1

xx = np.array(xx)
yy = np.array(yy)

plt.plot(xx, yy, 'r')

plt.title("PLOTTING OF THE FUNCTION THROUGH IT'S 1ST ORDER DIFFERENTIAL EQUATION AND BOUNDARY CONDITIONS")
plt.xlabel("x values        x axis --->")
plt.ylabel("f(x) values        y axis --->")
plt.legend(["y as a $function$ of x for n=500000,h=0.00001 "], loc="upper right")
plt.grid()

plt.show()
