import turtle as tr
import numpy as np
a = tr.Turtle()
a.speed(0)

a.penup()
a.goto(-64,-300)
a.pendown()

alp = 1.2   # put  alpha>1 (1<alp<2 would be nice)
l = 128
x = (1/(1+alp**2)**0.5)
angle = 180*np.arctan(alp)/np.pi
lim = 10


def tree(i):
    if i < lim:
        while i < lim:
            break
    else:
        for j in range(4):
            a.fd(i)
            a.lt(90)
        a.penup()
        for j in range(3):
            a.fd(i)
            a.lt(90)
        a.pendown()
        a.lt(90+angle)
        tree(i*x)                   # right portions
        a.rt(90+angle)
        a.penup()
        for j in range(3):
            a.fd(i)
            a.lt(90)
        a.rt(90-angle)
        a.fd(i*x*alp)
        a.pendown()
        a.lt(180)
        tree(i*x*alp)          # left portions
        a.penup()
        a.fd(i*x*alp)
        a.rt(90+angle)
        for j in range(2):
            a.fd(i)
            a.lt(90)
        a.pendown()


a.fillcolor('green')
a.begin_fill()
tree(l)
a.end_fill()
tr.done()
