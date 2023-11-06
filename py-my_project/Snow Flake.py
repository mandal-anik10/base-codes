import turtle as tr
import numpy as np

a = tr.Turtle()
# a.pencolor('blue')

a.penup()
a.goto(-243,-243*np.tan(np.pi/3)/3)
a.pendown()

for i in range(3):
    x= 729/3
    for j in range(10):
        x = x/3
        a.fd(x)
        a.lt(60)

    for k in range(10):
        a.rt(120)
        for m in range(2):
            a.fd(x)
            a.lt(60)
            x = x*3
tr.done()
