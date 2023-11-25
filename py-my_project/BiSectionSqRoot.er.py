
# DETERMINATION OF THE SQUARE ROOT OF A GIVEN NUMBER THROUGH BISECTION :


print("\n\tDETERMINATION OF THE SQUARE ROOT OF A GIVEN NUMBER THROUGH BISECTION :\n\n")

x=float(input("Please, Enter the your number as 'x' : "))

a=float(input("\nPlease, Enter any number as 'a' such that 'a^2<x' : "))
b=float(input("Please, Enter any number as 'b' such that 'b^2>x' : "))

esp=float(input("Please, Enter the value of maximum error : "))
err=1

while err > esp:
    c=(a+b)/2

    if c**2 < x:
        a=c
    elif c**2 == x:
        err=esp
    else :
        b=c
    err=abs(c**2-x)

print("\nThe value of the square root of",x,"is equals to :",c)