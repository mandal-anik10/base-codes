'''
PLOTTING OF THE FUNCTION OF RADIO-ACTIVE DECAY :

Author : Anik Mandal
'''

import matplotlib.pyplot as plt
import numpy as np

# BOUNDARY CONDITIONS :
x0 = x = 0.0
y0 = y = 10**5
l = 0.01

thf = 2.303*np.log10(2)/l

xx = []
yy = []

n = 70000
xs = 0.01
i = 1

while i <= n:
    xx.append(x)
    yy.append(y)

    # SLOPE OF THE GRAPH AT BOUNDARY CONDITION:
    m = -l*y

    c = y - m*x
    x = x + xs
    y = m*x + c

    i = i+1

xx = np.array(xx)
yy = np.array(yy)

plt.plot(xx, yy, 'r')

plt.suptitle("PLOTTING OF THE FUNCTION OF RADIO-ACTIVE DECAY :")
plt.title("Decay constant : "+str(l)+"$s^{-1}$    Half life : "+str(thf)+"s")
plt.xlabel("t values(s)        x axis --->")
plt.ylabel(" N[number of radioactive particles]        y axis --->")
plt.legend(["N($number of radioactive particles$) as a $function$ of t"])
plt.grid()
plt.show()
