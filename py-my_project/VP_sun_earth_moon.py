'''
Animation of motion of Sun-earth-moon system using Vpython

Author : Anik Mandal
'''

from vpython import *
from numpy import *
from random import*

canvas(tile ='orbit',
       width=1500,height=800,
       background=color.black)

e= sphere(pos = vector(0,200,0),radius = 5,color=color.cyan)
s= sphere(pos=vector(0,0,0),radius=50,color=color.yellow)
m = sphere(pos=vector(0,180,0),radius=1,color=color.white)
traile=curve(color=color.red)
trailm=curve(color=color.blue)

i = 1
while i < 1000000:
    e.pos = vector(200*cos(i*pi/180000),200*sin(i*pi/180000),0)
    m.pos = vector(200*cos(i*pi/180000) - 20*cos(13*i*pi/180000),200*sin(i*pi/180000),20*sin(13*i*pi/180000))

    traile.append(pos=e.pos)
    trailm.append(pos=m.pos)
    i = i+1