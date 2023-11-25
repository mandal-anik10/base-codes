
#DETERMINATION OF THE VALUE OF sin(x) WITH ERROR APPROXIMATION :


import math
print("\n\tDETERMINATION OF THE VALUE OF sin(x) WITH ERROR APPROXIMATION \n\n")

a=float(input("Please, enter the value of 'x' as angle in degree : "))
x=a*math.pi/180
esp=float(input("Please, enter the value of maximum error : "))

(i,fact,sum,err,z,tm)=(0,1,0,1,1,0)

while (err >= esp):
    i = i + 1
    fact = fact * i
    if i % 2 == 1:
        z=z+1
        t = (x ** i)*((-1)**z) / fact
        sum = sum + t
        err = abs(t)
        tm=tm+1

print("\nThe value of the sin(",a,") with maximum error approximation",esp," :\t",sum)
print("The total number of terms reqired to reach the accuracy :",tm)