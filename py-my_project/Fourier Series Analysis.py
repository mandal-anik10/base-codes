
# DETERMIANTION OF THE FOURIER SERIES COEFFICIENTS FOR GIVAN SITUATION AND BOUNDARY CONDITIONS :
# AND PLOTTING OF THE EXACT FOURIER FUNCTION FOR DIFFERENT VALUES OF x :

import matplotlib.pyplot as plt
import numpy as np
print("\n\tDETERMIANTION OF THE FOURIER SERIES COEFFICIENTS FOR GIVAN SITUATION AND BOUNDARY CONDITIONS :\n\n")

xi=-np.pi
xf=np.pi
n=10000
h=(xf-xi)/(n-1)
nc=500
xx=np.linspace(xi,xf,n)
#y=x
cc=[]
cs=[]
yy=[]


for i in range(nc):
    yc=np.cos(1.5*xx)*np.cos(i*xx)
    ys=np.cos(1.5*xx)*np.sin(i*xx)
    j=1
    (sc, ss) = (0, 0)
    while j<(n-1):
        k=j%2
        if k==1:
            sc=sc+4*yc[j]
            ss=ss+4*ys[j]
        else :
            sc=sc+2*yc[j]
            ss=ss+2*ys[j]
        j=j+1
    sc=(yc[0]+yc[n-1]+sc)*h/(3*np.pi)
    ss=(ys[0]+ys[n-1]+ss)*h/(3*np.pi)

    cc.append(sc)
    cs.append(ss)

cc[0]=cc[0]/2
yy=[]
print(cc,"\n",cs)
for i in range(n):
    s=0
    for j in range(nc):
        s=s+cc[j]*np.cos(j*xx[i])+cs[j]*np.sin(j*xx[i])
    yy.append(s)

print(xx)
print(yy)

plt.plot(xx,yy)
plt.show()

