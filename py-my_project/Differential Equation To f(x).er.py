
# PLOTTING OF THE FUNCTION THROUGH IT'S 1ST ORDER DIFFERENTIAL EQUATION AND BOUNDARY CONDITIONS :

import matplotlib.pyplot as plt
import numpy as np

print("\n\tPLOTTING OF THE FUNCTION THROUGH IT'S 1ST ORDER DIFFERENTIAL EQUATION AND BOUNDARY CONDITIONS\n\n")

# BOUNDARY CONDITIONS :
print("Please, Enter the boundary condition :")
x = float(input("\tWhen x ="))
y = float(input("\t\ty ="))

X = []
Y = []

n = int(input("Please, Enter the number of points to determine the graph of f(x) :"))
xs = float(input("Please, Enter the approximated small partitions of the x axis :"))
i = 1

while i <= n:
    X.append(x)
    Y.append(y)

    # SLOPE OF THE GRAPH AT BOUNDARY CONDITION:
    m = x-2*y

    c = y - m*x
    x = x + xs
    y = m*x + c

    i = i+1

X = np.array(X)
Y = np.array(Y)

plt.plot(X,Y,'r')
plt.title("PLOTTING OF THE FUNCTION THROUGH IT'S 1ST ORDER DIFFERENTIAL EQUATION AND BOUNDARY CONDITIONS")
plt.xlabel("x values        x axis --->")
plt.ylabel("f(x) values        y axis --->")
plt.legend(["y as a $function$ of x"])
plt.grid()
plt.show()