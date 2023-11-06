import numpy as np
import matplotlib.pyplot as plt

# Datas:
c = 3*10**8
v = 0.8*c
gm = 1/(1-(v/c)**2)**0.5
Ve = np.linspace(0, 2*c, 1000)          # Ve = L/T = space seperation/time seperation
T = 1

rL = gm*T*(Ve-v)
rT = gm*T*(1-(v*Ve)/(c**2))*10**8

plt.plot(Ve,rL,Ve,rT)
plt.grid()
plt.show()

