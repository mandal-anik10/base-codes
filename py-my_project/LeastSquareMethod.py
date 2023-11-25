
#DETERMINATION OF THE MEAN GRAPH USING LEAST SQUARE METHOD

import matplotlib.pyplot as plt
import numpy as np

print("\n\tDETERMINATION OF THE MEAN GRAPH USING LEAST SQUARE METHOD\n\n")
x=[]
y=[]
n=int(input("Please, Enter the number of element of your data sheet : "))

for i in range(n):
    print("Please, Enter the X[",i,"] element :",end="")
    e1=float(input())
    x.append(e1)
print("\n")
for j in range(n):
    print("Please, Enter the y[",j, "] element :",end="")
    e2 = float(input())
    y.append(e2)

x=np.array(x)
y=np.array(y)

(sumx,sumy,p1,p2)=(0,0,0,0)

for k in range(len(x)):
    sumx=sumx+x[k]
    sumy=sumy+y[k]

xb=sumx/len(x)
yb=sumy/len(y)

for l in range(len(x)):
    p1=p1+(x[l]-xb)*(y[l]-yb)
    p2=p2+(x[l]-xb)**2

m=p1/p2
c=yb-m*xb

x1=x
y1=m*x1+c

plt.plot(x,y,"*r",x1,y1,"-b")
plt.xlabel("x data --->")
plt.ylabel("y data --->")
plt.legend(["Experimental Data","Mean Graph"])
plt.title("Least Square Method")
plt.grid()
plt.show()