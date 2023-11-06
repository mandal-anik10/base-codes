# Diagram of Velocity Addition formula

import numpy as np
import matplotlib.pyplot as plt

c = 3*10**8
fv = np.linspace(-c, c, 50)
ov = np.linspace(-c, c, 1000)

for i in range(len(fv)):
    rv = np.zeros(len(ov))

    for j in range(len(ov)):
        y = (ov[j] - fv[i]) / (1 - (ov[j] * fv[i]) / c ** 2)
        rv[j] = y
    plt.plot(ov, rv)

plt.title("Object velocity w.r.t. several frames in motion")
plt.xlabel("Object velocity in Lab frame(m/s)")
plt.ylabel("Object velocity w.r.t. another frame(m/s)")
plt.grid()
plt.show()
