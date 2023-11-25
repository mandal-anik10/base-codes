
# DETERMINATION OF THE DIFFERENTIATION OF A FUNCTION AT A GIVEN POINT :


def f(x):               # function
    return x**3.0-3.0*x


a = float(input('Point: '))
h = 0.0000000001        # approximated h value

df = (f(a+h)-f(a))/h
print("\nSo, the differentiated value of the function at the point", a, "is : ", df)
