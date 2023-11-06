import turtle as tr
import numpy as np

at = tr.Turtle()
bt = tr.Turtle()
at.speed(0)
bt.speed(0)
a = [at, bt]


c1 = []
c2 = []

for i in range(2):
    a[i].penup()
    a[i].goto(0,-128)
    a[i].pendown()
    a[i].pencolor('indigo')
    a[i].fillcolor('brown')

    a[i].begin_fill()

    if i==1:
        a[i].lt(180)
        a[i].fd(128)
        a[i].rt(90)
    else:
        a[i].fd(128)
        a[i].lt(90)
    x=256
    for j in range(20):
        if i==1:
            c1.append(a[i].pos())
        else:
            c2.append(a[i].pos())



        a[i].fd(x)
        x = (x * 2 ** 0.5) / 2
        if i==1:
            a[i].lt(45)
        else:
            a[i].rt(45)

    if i == 1:
        a[i].lt(-135)
    else:
        a[i].rt(-135)
    for k in range(20):
        x = (x*2**0.5)
        for m in range(3):

            a[i].fd(x)
            if i == 1:
                a[i].rt(90)
            else:
                a[i].lt(90)

        if i == 1:
            a[i].rt(135)
        else:
            a[i].lt(135)

    a[i].end_fill()
tr.done()
