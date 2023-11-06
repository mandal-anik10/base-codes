
# DETERMINATION OF THE VALUE OF INTEGRATION OF A FUNCTION THROUGH SIMPSON 1/3 METHON :


print("\n\tDETERMINATION OF THE VALUE OF INTEGRATION OF A FUNCTION THROUGH SIMPSON 1/3 METHON :\n\n")


xi = 0.0
xf = 10.0

n = 10000
h = (xf-xi)/(n-1.0)

yi = xi**2.0-5.0*xi+7.0
yf = xf**2.0-5.0*xf+7.0

# Suppose,
#    my function is : yi=f(xi)=xi^2-5*xi+7

(i, s) = (1, 0.0)

while i < (n-1):
    c = xi+i*h
    yc = c**2.0-5.0*c+7.0

    if i % 2.0 == 1.0:
        s = s+4.0*yc
    else:
        s = s+2.0*yc
    i = i+1

s = (yi+yf+s)*h/3.0

print("\nThe value of the integration of my function from", xi, "to", xf, "is equals to : ", s)
