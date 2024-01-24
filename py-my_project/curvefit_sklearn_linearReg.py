'''
Curve fitting using scikit-learn LinearRegression

Author : Anik Mandal
'''

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

n = 200
x_data = np.linspace(-3, 3, n)[:, None]
y_data = np.exp(-x_data ** 2) + 0.05 * np.random.randn(n, 1)

# x_new= np.hstack([x_data,x_data**2,x_data**3,x_data**4,x_data**5,x_data**6,x_data**7,x_data**8,x_data**9,x_data**10])
poly = PolynomialFeatures(degree=10, include_bias=False)
x_new = poly.fit_transform(x_data)

mdl = LinearRegression().fit(x_new, y_data)

m = mdl.coef_
c = mdl.intercept_
print(m, c)
xx = np.linspace(-3, 3, 100)
yy = []
for i in range(len(xx)):
    a = 0
    for j in range(len(m[0])):
        a = a + (m[0][j] * xx[i] ** (j + 1))
    yy.append(a + c[0])
plt.plot(x_data, y_data, '+r', xx, yy, 'c')
plt.suptitle('Curve fitting using SkLearn(Linear Regression)')
plt.legend(['$Experimental Data$', 'Predicted Model'], loc=2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
