# Logo Design:


import matplotlib.pyplot as plt
import
import numpy as np

## functions:
xi = -12
xf = 12
n = 1000
ncv = 25
nc = ncv

xx = np.linspace(xi,xf,n)

Yuc = (xi**2-xx**2)**0.5
Ydc = -Yuc

yug = Yuc-np.cos(xx*np.pi/20)-3*np.exp(-abs(xx-7)/2)
ydg = Ydc+2*np.cos(xx*np.pi/20)+12*np.exp(-abs((xx-7)/2))


## fourier:
# cu = Fourier(Yuc,xi,xf,n,ncv)
# cd = Fourier(Ydc,xi,xf,n,ncv)

iu = Fourier(yug,xi,xf,n,nc)
id = Fourier(ydg,xi,xf,n,nc)

## ellipse:
## small circles:
xs = np.linspace(6.5,7.5,100)
su = (0.5**2-(xs-7)**2)**0.5+5
sd = -(0.5**2-(xs-7)**2)**0.5+5
## big circle:
cu = (12**2-xx**2)**0.5
cd = -cu
plt.plot(xs,su,'k',xs,sd,'k')
plt.plot(xx,iu[2],'k',xx,id[2],'k')
plt.plot(xx,cu,'k',xx,cd,'k')
plt.xlim(-15,15)
plt.ylim(-15,15)
plt.show()
