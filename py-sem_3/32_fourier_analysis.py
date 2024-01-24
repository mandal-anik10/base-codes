'''
DETERMINATION OF THE FOURIER SERIES COEFFICIENTS FOR GIVAN SITUATION AND BOUNDARY CONDITIONS :
AND PLOTTING OF THE EXACT FOURIER FUNCTION FOR DIFFERENT VALUES OF x :

Author : Anik Mandal
'''
import matplotlib.pyplot as plt
import numpy as np

xi = -np.pi
xf = np.pi

n = 1000
h = (xf-xi)/(n-1)
nc = 25

xx = np.linspace(xi, xf, n)
# y=xx^3
cc = []
cs = []
yy = []


for i in range(nc):
    yc = (xx**3)*np.cos(i*xx)
    ys = (xx**3)*np.sin(i*xx)

    j = 1
    (sc, ss) = (0, 0)

    while j < (n-1):
        k = j % 2

        if k == 1:
            sc = sc+4*yc[j]
            ss = ss+4*ys[j]

        else:
            sc = sc+2*yc[j]
            ss = ss+2*ys[j]

        j = j+1

    sc = (yc[0]+yc[n-1]+sc)*h/(3*np.pi)
    ss = (ys[0]+ys[n-1]+ss)*h/(3*np.pi)

    cc.append(sc)
    cs.append(ss)

cc[0] = cc[0]/2
yy = []
zz = xx**3

print("Coefficients of cosine function : ", cc, "\nCoefficients of sine function : ", cs)

for i in range(n):
    s = 0

    for j in range(nc):
        s = s + cc[j]*np.cos(j*xx[i]) + cs[j]*np.sin(j*xx[i])

    yy.append(s)

plt.plot(xx, yy, '-r', xx, zz, '-.b')

plt.title("FOURIER ANALYSIS OF A FUNCTION"+"\nNumber of points :"+str(n)+" Number of coefficients :"+str(nc))
plt.xlabel("x Data --->")
plt.ylabel("y Data --->")
plt.legend(["Fourier function", "Actual function"])
plt.grid()

plt.show()
