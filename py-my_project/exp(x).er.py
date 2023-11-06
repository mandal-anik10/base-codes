
#DETERMINATION OF THE VALUE OF exp(x) WITH ERROR APPROXIMATION :


print("\n\tDETERMINATION OF THE VALUE OF exp(x) WITH ERROR APPROXIMATION \n\n")

x=float(input("Please, enter the value of 'x' as the power of 'e' : "))
esp=float(input("Please, enter the value of maximum error : "))

(i,fact,sum,err,tm)=(1,1.0,1,1,0)

while (err>=esp):
    fact=fact*i
    t=(x**i)/fact
    sum=sum+t
    err=abs(t)
    i=i+1
    tm=tm+1

print("\nThe value of the exp(",x,") with maximum approximation",esp," :\t",sum)
print("The total number of terms reqired to reach the accuracy :",tm)