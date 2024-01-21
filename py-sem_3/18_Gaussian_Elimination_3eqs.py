'''
DETERMINATION OF THE VALUE OF x,y FROM TWO LINEAR EQUATION THROUGH GAUSSIAN ELIMINATION METHOD :

Author : Anik Mandal
'''
x = 1.0
y = 2.0
z = 3.0

eps = 1e-5
erx = ery = erz = 1.0

# My equations are:
#       12x+3y-5z=1         (1)
#       x+5y+3z=28          (2)
#       3x+7y+13z=76        (3)

while erx and ery and erz > eps:

    x1 = (1.0-3.0*y+5.0*z)/12.0
    y1 = (28.0-x1-3.0*z)/5.0
    z1 = (76.0-3.0*x1-7.0*y1)/13.0

    erx = abs(x-x1)
    ery = abs(y-y1)
    erz = abs(z-z1)

    x = x1
    y = y1
    z = z1

print("So, the general solution of my equations are x =", x, "y =", y, "z =", z)
