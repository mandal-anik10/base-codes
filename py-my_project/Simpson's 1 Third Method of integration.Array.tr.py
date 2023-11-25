
# DETERMINATION OF THE VALUE OF INTEGRATION OF A FUNCTION THROUGH SIMPSON 1/3 METHON USING ARRAY:

import numpy as np

print("\n\tDETERMINATION OF THE VALUE OF INTEGRATION OF A FUNCTION THROUGH SIMPSON 1/3 METHON :\n\n")


xi = float(input("Please, Enter the lower limit of integration as xi: "))
xf = float(input("Please, Enter the higher limit of integration as xf : "))

n = int(input("Please, Enter the total number of points : "))
h = (xf-xi)/(n-1)
xx=np.linspace(xi, xf, n)

# Suppose,
#    my function is : yi=f(xi)=xi
yy=xx

(i,s)=(1,0)

while i<n-1:
    k=i%2
    if k==1:
        s=s+4*yy[i]
    else:
        s=s+2*yy[i]
    i=i+1

s = (yy[0]+yy[n-1]+s)*h/3

print("\nThe value of the integration of my function from",xi,"to",xf,"is equals to : ",s)