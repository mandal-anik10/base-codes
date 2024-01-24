'''
This script will generate a symmetric Pythagorean Tree using Turtle.

Author : Anik Mandal
'''

import turtle as tr

a = tr.Turtle()     # calling Turtle object
a.speed(0)          # definig speed of the turtle motion, 0 is maximum and speed increses from 0 to 10

a.penup()
a.goto(-64,-300)
a.pendown()

l_max = 128     # maximum length
l_min = 8     # minimum length

def tree(i, lim):
    '''
    This function works in a nested way to create the Pythagorean Tree.
    -----Inputs--------------------------------------------------------
    i : float 
        Maximum size of the Pythagorean Tree
    lim : float
        Minimum size to be considered
    '''
    if i<lim:
        exit
    else:
        for j in range(4):
            a.fd(i)
            a.lt(90)
        a.penup()
        for j in range(3):
            a.fd(i)
            a.lt(90)
        a.pendown()
        a.lt(135)

        tree(i = i/2**0.5, lim = lim)               # right portions

        a.rt(135)
        a.penup()
        for j in range(3):
            a.fd(i)
            a.lt(90)
        a.rt(45)
        a.fd(i/2**0.5)
        a.pendown()
        a.lt(180)

        tree(i = i/2**0.5, lim = lim)               # left portions

        a.penup()
        a.fd(i / 2 ** 0.5)
        a.rt(135)
        for j in range(2):
            a.fd(i)
            a.lt(90)
        a.pendown()

a.fillcolor('indigo')
a.begin_fill()
tree(i = l_max, lim=l_min)
a.end_fill()

tr.done()
