
# DETERMINATION OF THE VALUE OF SQUARE ROOT OF A GIVEN NUMBER THROUGH NEWTON-RAPHSON METHOD WITH ERROR APPROXIMATION :

import matplotlib.pyplot as plt
import numpy as np

print("\n\tDETERMINATION OF THE VALUE OF SQUARE ROOT OF A GIVEN NUMBER THROUGH NEWTON-RAPHSON METHOD WITH ERROR APPROXIMATION :\n\n")

n=float(input("Please, Enter your number as 'n' : "))

x=float(input("\nPlease, Enter any number 'x' such that x^2>n : "))
eps=float(input("Please, Enter the the value of maximum error in the calculation : "))
(err,i)=(1,1)
X=[]
Y=[]
while err>eps:
    x1=x
    m=2*x1
    y=x1**2-n

    X.append(x1)
    Y.append(y1)

    x=x1-(y/m)
    err=abs(y)
print("The value of square root of",n,"is : ",x)

