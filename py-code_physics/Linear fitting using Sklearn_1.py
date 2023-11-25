##

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Creating Sample Experimental Data:
x_data = np.array([[1], [2], [3], [4], [5], {6}])
y_data = 2 * x_data + 3 + 0.5 * np.random.randn(6, 1)

mdl = LinearRegression().fit(x_data, y_data)

m = mdl.coef_
c = mdl.intercept_
print(m, c)
xx = np.linspace(1, 6, 100)
yy = []
for i in range(len(xx)):
    yy.append(m[0][0] * xx[i] + c[0])

plt.plot(x_data, y_data, '+r', xx, yy, 'c')
plt.show()
