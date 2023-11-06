
# DETERMINATION OF THE VALUE OF ln(x) WITH ERROR APPROXIMATION:


print("\n\tDETERMINATION OF THE VALUE OF ln(x) WITH ERROR APPROXIMATION:\n\n")

a = float(input("Please, Enter the value of the number(x) :  "))
if a>=1:
    x = 1 - (1/a)
else :
    x=1-a

esp = float(input("Please, Enter the value of the maximum error :  "))
(err, sum, i, tm) = (1, 0, 1, 0)

while err >= esp:
    t = (x**i)/i
    sum = sum+t
    i = i+1
    err = abs(t)
    tm=tm+1
if a>=1 :
    print("\nThe value of the ln(", a, ") :  ", sum)
else :
    print("\nThe value of the ln(", a, ") :  ", -sum)
print("The total number of terms reqired to reach the accuracy :",tm)

