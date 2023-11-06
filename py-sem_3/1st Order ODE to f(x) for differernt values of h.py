
# PLOTTING OF THE FUNCTION THROUGH IT'S 1ST ORDER DIFFERENTIAL EQUATION AND BOUNDARY CONDITIONS :


import matplotlib.pyplot as plt
import numpy as np

# BOUNDARY CONDITIONS :
x = x1 = 0.0
y = y1 = 0.0

xx = []
yy = []

xx1 = []
yy1 = []

n = 1000000
xs = 0.00001

n2 = 50
xs1 = 0.2

i = 1
j = 1
while i <= n:
    xx.append(x)
    yy.append(y)

    # SLOPE OF THE GRAPH AT BOUNDARY CONDITION:
    m = np.sin(x)-2*y

    c = y - m*x
    x = x + xs
    y = m*x + c

    i = i+1

while j <= n2:
    xx1.append(x1)
    yy1.append(y1)

    # SLOPE OF THE GRAPH AT BOUNDARY CONDITION:
    m1 = np.sin(x1)-2*y1

    c1 = y1 - m1*x1
    x1 = x1 + xs1
    y1 = m1*x1 + c1

    j = j+1

xx1 = np.array(xx1)
yy1 = np.array(yy1)

xx = np.array(xx)
yy = np.array(yy)

plt.plot(xx, yy, 'r')
plt.plot(xx1, yy1, 'b')
plt.title("PLOTTING OF THE FUNCTION THROUGH IT'S 1ST ORDER DIFFERENTIAL EQUATION AND BOUNDARY CONDITIONS")
plt.xlabel("x values        x axis --->")
plt.ylabel("f(x) values        y axis --->")
plt.legend(["y as a $function$ of x : for n=1000000,h=0.00001", "y as a $function$ of x : for n=50,h=0.2"], loc="lower left")
plt.grid()
plt.show()
