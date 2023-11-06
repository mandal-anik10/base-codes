
# DETERMINATION OF THE VALUE OF INTEGRATION OF A FUNCTION THROUGH SIMPSON 1/3 METHON :


print("\n\tDETERMINATION OF THE VALUE OF INTEGRATION OF A FUNCTION THROUGH SIMPSON 1/3 METHON :\n\n")


xi = float(input("Please, Enter the lower limit of integration as xi: "))
xf = float(input("Please, Enter the higher limit of integration as xf : "))

n = int(input("Please, Enter the total number of points : "))
h = (xf-xi)/(n-1)

yi = xi
yf = xf

# Suppose,
#    my function is : yi=f(xi)=xi

(i,s)=(1,0)

while i<(n-1):
    c = xi+i*h
    yc = c

    if i%2 == 1:
        s=s+4*yc
    else:
        s=s+2*yc
    i=i+1

s = (yi+yf+s)*h/3

print("\nThe value of the integration of my function from",xi,"to",xf,"is equals to : ",s)