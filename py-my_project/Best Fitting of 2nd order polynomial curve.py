

import numpy as np
import matplotlib.pyplot as plt

#Experimental Datas:
xx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
yy = [-8, -5, 0, 5, 17, 25, 40, 55, 72, 88]

(sx, sy, sxs, sys, xtu, ytu, xtd, au, ad) = (0, 0, 0, 0, 0, 0, 0, 0, 0)
for i in range(len(xx)):
    sx = sx + xx[i]
    sy = sy + yy[i]
    sxs = sxs + xx[i]**2
    sys = sys + yy[i]**2
avx = sx/len(xx)
avy = sy/len(yy)
avxs = sxs/len(xx)
avys = sys/len((yy))

for i in range(len(xx)):
    ytu = ytu + xx[i]*(yy[i]-avy)
    xtu = xtu + xx[i]*(xx[i]**2-avxs)
    xtd = xtd + xx[i]*(xx[i]-avx)
xt = xtu/xtd
yt = ytu/xtd

for i in range(len(xx)):
    au = au +(xx[i]**2)*(yy[i]-yt*xx[i]-avy+yt*avx)
    ad = ad +(xx[i]**2)*(xx[i]**2+xt*xx[i]-avxs-xt*avx)

a = au/ad
b = yt+a*xt
c = avy-a*avxs-b*avx
print(a,b,c)

zz = []
for i in range(len(xx)):
    z = a*xx[i]**2+b*xx[i]+c
    zz.append(z)

plt.plot(xx,yy,'.r')
plt.plot(xx,zz,'g')
plt.show()