# Curve Fitting of Major axis vs Time period data of planets:

from scipy.optimize import *
from matplotlib.pyplot import *
import numpy as np
import pandas as pd

x = pd.read_csv(r'C:\Users\Anik Mandal\OneDrive\Documents\MS Office\Office Excel\Planet Data_1.csv')
print(x)
x_data = x['Major Axis,A (AU)'].values
y_data = x['Time Period (Earth Year)'].values


def func(x_value, a, b, cons):
    y = a * x_value ** b + cons
    return y


# ig = [1, 1, 1]
c, cov = curve_fit(func, x_data, y_data)
print(c)

xx = np.linspace(0.77, 79, 100)
yy = func(xx, c[0], c[1], c[2])

plot(x_data, y_data, '.r', xx, yy, 'c')
grid()
suptitle('Major Axis,A (AU) vs Time Period (Earth Year)')
legend(['Actual Data', 'Mean Graph\nT =' + str(c[0]) + '*A^' + str(c[1]) + '+(' + str(c[2]) + ')'])
xlabel('Major Axis,A (AU)')
ylabel('Time Period (Earth Year)')
show()
