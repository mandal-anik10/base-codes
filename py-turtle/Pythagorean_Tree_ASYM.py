'''
This script will generate an asymmetric Pythagorean Tree using Turtle.

Author : Anik Mandal
'''

import turtle as tr
import numpy as np

a = tr.Turtle()     # calling Turtle object
a.speed(0)          # definig speed of the turtle motion, 0 is maximum and speed increses from 0 to 10

a.penup()
a.goto(-64,-300)
a.pendown()

alp = 1.2   # put  alpha>1 (1<alp<2 would be nice)
l_max = 128     # maximum length
x = (1/(1+alp**2)**0.5)
angle = 180*np.arctan(alp)/np.pi
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
    if i < lim:
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
        a.lt(90+angle)

        tree(i = i*x, lim = lim)                    # right portions

        a.rt(90+angle)
        a.penup()
        for j in range(3):
            a.fd(i)
            a.lt(90)
        a.rt(90-angle)
        a.fd(i*x*alp)
        a.pendown()
        a.lt(180)
        
        tree(i = i*x*alp, lim = lim)                # left portions
        
        a.penup()
        a.fd(i*x*alp)
        a.rt(90+angle)
        for j in range(2):
            a.fd(i)
            a.lt(90)
        a.pendown()


a.fillcolor('green')
a.begin_fill()
tree(i = l_max, lim = l_min)
a.end_fill()

tr.done()
