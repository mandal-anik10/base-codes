import numpy as np
import turtle as tr
a = tr.Turtle()

for i in range(2):
    for j in range(10):
        pp.append(a.pos())
        if i == 0:

            a.penup()
            a.goto(pp[4*j-1])
            a.lt(45*(1-j))
            a.pendown()

            for k in range(4):
                a.fd(x/(2**((j+1)/2)))
                a.lt(90)

        a.seth(0)

        # else:
        #     a.penup()
        #     if j ==0:
        #         a.goto(pp[2])
        #         a.lt(-45)
        #     else:
        #         a.goto(pp[4*j])
        #         a.lt(-180)
        #     a.pendown()
        #     for k in range(4):
        #         pp.append(a.pos())
        #         a.fd(256/(2))
        #         a.lt(90)
