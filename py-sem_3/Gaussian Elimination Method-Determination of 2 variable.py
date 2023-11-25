
# DETERMINATION OF THE VALUE OF x,y FROM TWO LINEAR EQUATION THROUGH GAUSSIAN ELIMINATION METHOD :


print("\n\tDETERMINATION OF THE VALUE OF x,y FROM TWO LINEAR EQUATION THROUGH GAUSSIAN ELIMINATION METHOD :\n")

x = 1.0
y = 0.0

eps = 0.00001
erx = ery = 1.0

# My equations are:
#       8x+3y=7     (1)
#       x+10y=3     (2)
while erx and ery > eps:

    x1 = (7.0-3.0*y)/8.0
    y1 = (3.0-x)/10.0

    erx = abs(x-x1)
    ery = abs(y-y1)

    x = x1
    y = y1

print("So, the general solution of my equations are x =", x, "y =", y)
