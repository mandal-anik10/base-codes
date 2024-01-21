'''
DETERMINATION OF THE DIFFERENTIATION OF A FUNCTION AT A GIVEN POINT :

Author : Anik Mandal
'''

def f(x):               # function
    return x**3.0-3.0*x


a = float(input('Point: '))
h = 1e-5        # approximated h value

df = (f(a+h)-f(a-h))/(2*h)
print("\nSo, the differentiated value of the function at the point", a, "is : ", df)
