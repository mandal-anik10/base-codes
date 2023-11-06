

from LocalModule.Curve_FIt import Nonlinear_Fit
import numpy as np
import matplotlib.pyplot as plt
xi = -3
xf = 3
n = 200
v_list = np.array([20 * i for i in range(60)])
print(v_list)
v_list = v_list[:,None]
print(v_list)
nn = ((v_list/500)**2)*np.exp(-(v_list/500)**2)+np.random.uniform(-5,6)
print(nn)
d = 10

f, g = Nonlinear_Fit(v_list, nn, n, d, 0.001)

plt.plot(v_list, nn, '+', f, g, 'r')
plt.suptitle('Curve fitting using SkLearn(Lasso)')
# plt.title('Max power of x:'+str(d)+'    Alpha Value:'+str(alp))
plt.legend(['$Observed Experimental Data$', '$Predicted Model$'], loc=1)
plt.grid()
plt.show()
