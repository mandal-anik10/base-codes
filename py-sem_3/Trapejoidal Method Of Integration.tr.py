
# DETERMINATION OF THE VALUE OF INTEGRATION OF A FUNCTION THROUGH TRAPEZOIDAL METHOD :

xi = float(input('Initial point: ',))
xf = float(input('Final point: ',))

n = int(input('Approximation(No. of points): ',))
h = (xf-xi)/(n-1)

# Suppose,
#   My function is : yi=f(xi)=xi^2

yi = xi**2
yf = xf**2

(i, err, s) = (1, 1.0, 0.0)

while i < (n-1):
    c = xi+i*h
    fc = c**2
    s = s+fc
    i = i+1

s = (yi+yf+2*s)*h/2

print("\nThe value of the integration of my function from", xi, "to", xf, " is : ", s)
