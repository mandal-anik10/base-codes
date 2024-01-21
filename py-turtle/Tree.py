'''
This script will generate an stream-like asymmetric Pythagorean Tree using Turtle.

Author : Anik Mandal
'''

import turtle as tr

a = tr.Turtle()     # calling Turtle object
a.speed(0)          # definig speed of the turtle motion, 0 is maximum and speed increses from 0 to 10

a.lt(90)
a.penup()
a.backward(300)
a.pendown()

l_max = 128     # maximum length
l_min = 8     # minimum length

l = 0.80            # left branch size reduction
r = 0.70            # right branch size reduction
angle = 15

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
        if i > 100:
            a.pencolor('brown')
            a.pensize(i/15)
            a.fd(i)
            a.lt(angle)

            tree(i = i * l, lim = lim)              # right portions       
            a.rt(2*angle)
            tree(i = i * r, lim = lim)              # left portions

            a.lt(angle)
            a.penup()
            a.backward(i)
            a.pendown()
        else:
            a.pencolor('green')
            a.pensize(i/15)
            a.fd(i)
            a.lt(angle)

            tree(i = i * l, lim = lim)              # right portions
            a.rt(2*angle)
            tree(i = i * r, lim = lim)              # left portions

            a.lt(angle)
            a.penup()
            a.backward(i)
            a.pendown()

tree(i = l_max, lim = l_min)

tr.done()