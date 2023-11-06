
# DTERMINATION OF THE VALUE OF INTEGRATION OF A FUNCTION THROUGH TRAPEJOIDAL METHOD :


print("\n\tDTERMINATION OF THE VALUE OF INTEGRATION OF A FUNCTION THROUGH TRAPEJOIDAL METHOD :\n\n")

xi = float(input("Please, Enter the lower limit of the integration as 'xi' : "))
xf = float(input("please, Enter the higher limit of the integration as 'xf' : "))

n = int(input("Please, Enter the number of points as 'n' : "))
h = (xf-xi)/(n-1)

# Suppose,
#   My function is : yi=f(xi)=xi^2

yi = xi**2
yf = xf**2

(i, err, s) = (1, 1, 0)

while i < (n-1):
    c=xi+i*h
    fc=c**2
    s=s+fc
    i=i+1

s=(yi+yf+2*s)*h/2

print("\nThe value of the integration of my function from",xi,"to",xf," is : ",s)



