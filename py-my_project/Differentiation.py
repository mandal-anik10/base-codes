
# DETERMINATION OF THE DIFFERENTIATION OF A FUNCTION AT A GIVEN POINT :

print("\n\tDETERMINATION OF THE DIFFERENTIATION OF A FUNCTION AT A GIVEN POINT :\n\n")

def f(x):
    return x**3-3*x

a=float(input("Please, Enter the value of the given point where we want to find the differentiated value of the function :"))
h=float(input("Please, Enter a number 'h' such that the value of h is h -> 0 : "))

df=(f(a+h)-f(a))/h
print("\nSo, the differentiated value of the function at the point",a,"is : ",df)