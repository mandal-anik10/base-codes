
import numpy as np
from vpython import *
canvas(title = 'Relativistic mass and distortion of orbit of a star(G as unit)',
       height = 750, width = 1500)


def Grav_F(o1,o2):
    G = 1
    c = 3*10
    r_vec = o1.pos-o2.pos
    r_mag = mag(r_vec)
    r_hat = r_vec/r_mag
    gamma = 1/(1-(mag(o1.momentum)/(c*o1.mass))**2)**0.5
    f_mag = G*o1.mass*o2.mass/r_mag**2 
    f_vec = -f_mag*r_hat
    return f_vec


BH = sphere(pos = vector(0,0,0),
            radius = 0.1,
            mass = 500000,
            momentum = vector(0,-1,0),
            color = color.black,
            make_trail = True)
star = sphere(pos = vector(10,0,0),
              radius = 0.1,
              mass = 10,
              momentum = vector(0,1,0),
              color = color.yellow,
              make_trail = True)

BH_l = label(pos = BH.pos,
             text = 'Black Hole',yoffset = 25)
star_l = label(pos = star.pos,
               text = 'Star',yoffset = 25)

dt = 0.001
t = 0

while(True):
    rate(5000)
    
    BH.force = Grav_F(BH,star)
    star.force = Grav_F(star,BH)
    
    BH.momentum = BH.momentum + BH.force*dt
    star.momentum = star.momentum + star.force*dt
    
    BH.pos = BH.pos + BH.momentum*dt/BH.mass
    star.pos = star.pos + star.momentum*dt/star.mass
    
    BH_l.pos = BH.pos
    star_l.pos = star.pos

    t = t+dt
