'''
Shooting method: Inf Well Potential QM
With slider for different eigen states

Author : Anik Mandal
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
plt.subplots_adjust(0.10, 0.25)

# boundary conditions:
xi = 0
xf = 1
yi = 0
yf = 0

def y2p(x, y, yp, energy):
    p2 = -2 * energy * y        # ODE
    return p2


def Euler_Approx(x_initial, x_final, num_point, y_initial, yp_initial, energy):
    xn = x_initial
    yn = y_initial
    ypn = yp_initial
    y2pn = y2p(xn, yn, ypn, energy)
    xx = np.linspace(x_initial, x_final, num_point)
    h = xx[1] - xx[0]
    yy = [yi]

    for i in range(1, num):
        xn = xn + h
        yn = yn + ypn * h
        ypn = ypn + y2pn * h
        y2pn = y2p(xn, yn, ypn, energy)

        yy.append(yn)

    Y1 = yn
    return [xx, yy, Y1]


num = 1 + 2 ** 12
ee = np.linspace(0, 200, num)         # Range of energy values
alp = 1         # yp_initial(assumed, any non-zero positive value as long as y2p doesn't depend on yp)
Y_err = []      # List to store error value in y_final

for i in range(len(ee)):
    err = Euler_Approx(xi, xf, num, yi, alp, ee[i])[2] - yf
    Y_err.append(err)


# print(ee,Y_err)
# plt.plot(ee, Y_err)       # Energies vs error in final output


# Scanning: Of Eigen_Values
def Eigen_energies(Y_error):
    Eigen_e = []
    Err = []
    for i in range(1, len(Y_error)-1):
        (er_a, er_b, er_c) = (abs(Y_error[i-1]), abs(Y_error[i]), abs(Y_error[i+1]))
        if er_b < er_a and er_b < er_c:
            Eigen_e.append(ee[i])
            Err.append(Y_error[i])
    return Eigen_e, Err


Eigen_e = Eigen_energies(Y_err)[0]
print('Eigen Energies: ', Eigen_e)

# Plotting:
# Eigen function plot:
n = 1       # Define Eigen State(1=ground, 2=1st_excited,...)
a = Eigen_e[n-1]
x_data = Euler_Approx(xi, xf, num, yi, alp, a)[0]
y_data = Euler_Approx(xi, xf, num, yi, alp, a)[1]
ef, = ax1.plot(x_data, y_data, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel(r'$\psi$ (x)')
plt.suptitle('Inf. wall potential: Eigen Functions')
ax1.grid()
# Eigen value plot:
ax2.plot(np.arange(1, len(Eigen_e)+1)**2, Eigen_e, '-r', marker='o')
ax2.set_xlabel(r'square of the Quantum Number ($n^2$)')
ax2.set_ylabel('Eigen Energy')
ax2.set_ylim([0, np.max(Eigen_e)*1.1])
ax2.grid()

ax1.margins(x=0)
ax2.margins(x=0)

axn = plt.axes([0.10, 0.1, 0.75, 0.03], facecolor='yellow')
sn = Slider(axn, 'Quantum Number', 1, len(Eigen_e), valinit=n, valstep=1)


def update(val):
    # This function changes plot based on slider value
    n = sn.val
    a = Eigen_e[n-1]
    x_data = Euler_Approx(xi, xf, num, yi, alp, a)[0]
    y_data = Euler_Approx(xi, xf, num, yi, alp, a)[1]
    ef.set_xdata(x_data)
    ef.set_ydata(y_data)
    ax1.set_ylim([np.min(y_data)*1.1, np.max(y_data)*1.1])

    fig.canvas.draw_idle()

sn.on_changed(update)

plt.show()
