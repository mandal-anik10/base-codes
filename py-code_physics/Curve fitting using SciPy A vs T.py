# Curve Fitting of Major axis vs Time period data of planets:

from scipy.optimize import *
from matplotlib.pyplot import *
import numpy as np
import pandas as pd

a = pd.read_excel(r'C:\Users\Anik Mandal\Desktop\val.xlsx')
print(a)
x_data = a['Time(s)'].values
y_data = a['Velocity(m/s)'].values


def func(x_value, m, b, cons):
    y = m * x_value ** b + cons
    return y


ig = [1, 1, 1]
c, cov = curve_fit(func, x_data, y_data, ig)
print(c)

xx = np.linspace(0, 20, 100)
yy = func(xx, c[0], c[1], c[2])

plot(x_data, y_data, '.r', xx, yy, 'c')
grid()
##suptitle('Major Axis,A (AU) vs Time Period (Earth Year)')
##legend(['Actual Data', 'Mean Graph\nT =' + str(c[0]) + '*A^' + str(c[1]) + '+(' + str(c[2]) + ')'])
##xlabel('Major Axis,A (AU)')
##ylabel('Time Period (Earth Year)')
show()
