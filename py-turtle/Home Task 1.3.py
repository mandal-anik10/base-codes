#Turtle project 3
from turtle import *
from numpy import *
from distance import *

a = Turtle()
a.speed(0)
x = 100
pp =[]


a.penup()
a.goto(-x/2,-x/2)
a.pendown()

for i in range(4):
    pp.append(a.pos())
    a.fd(x)
    a.lt(90)

#####
for j in range(10):
    a.seth(0)
    a.penup()
    if j ==0:
        a.goto(pp[2])
    else:
        a.goto(pp[4*j])
    a.lt(45-45*j)
    a.pendown()

    for i in range(4):
        a.fd(x/(2**(j/2+1/2)))
        a.lt(90)
        pp.append(a.pos())


for j in range(10):
    a.seth(0)
    a.penup()
    if j ==0:
        a.goto(pp[2])
    else:
        a.goto(pp[4*j+1])
    a.lt(45-45*j)
    a.pendown()
    for k in range(10-j):
        for i in range(4):
            a.fd(x/(2**(j/2+1/2)))
            a.lt(90)
            pp.append(a.pos())



done()
