
import numpy as np
import matplotlib.pyplot as plt

x = y = np.linspace(0, 2*np.pi, 10)
x, y = np.meshgrid(x, y)

fx = np.sin(x)
fy = np.cos(y)
f_mag = (fx**2+fy**2)**0.5
plt.figure(figsize=(8,8))
plt.quiver(x, y, fx, fy, pivot='middle')
# plt.streamplot(x, y, fx, fy, density=1)
# plt.imshow(f_mag,cmap='gray')
plt.quiverkey(0, 1, 1, 1, label="=1m/s")
plt.axis('scaled')
plt.show()
