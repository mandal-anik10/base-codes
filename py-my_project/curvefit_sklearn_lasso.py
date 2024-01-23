'''
Curve fitting using scikit-learn Lasso

Author : Anik Mandal
'''
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

xi = -3
xf = 3
n = 200
x_data = np.linspace(xi, xf, n)[:, None]
y_data = 3*x_data**2-3*x_data**1+10*np.exp(-(x_data-1)**2)+0.5*np.random.randn(n, 1)

d = 10
poly = PolynomialFeatures(degree=d, include_bias=False)
x_new = poly.fit_transform(x_data)

alp = 0.1
sl = Lasso(alpha=alp).fit(x_new, y_data)

m = sl.coef_
c = sl.intercept_
s = sl.score(x_new, y_data)
print(m, c, s)

xx = np.linspace(xi, xf, n)
yy = []
for i in range(len(xx)):
    a = 0
    for j in range(len(m)):
        a = a + m[j]*xx[i]**(j+1)
    yy.append(a+c[0])

plt.plot(x_data, y_data, '+', xx, yy, 'r')
plt.suptitle('Curve fitting using SkLearn(Lasso)')
plt.title('Max power of x:'+str(d)+'    Alpha Value:'+str(alp))
plt.legend(['$Observed Experimental Data$', '$Predicted Model$'], loc=1)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
