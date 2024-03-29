
'''
Vpython simulation : central force motion
Star-planet system

Author : Anik Mandal
'''

from vpython import *

canvas(height = 750,width = 1500)
e_graph = gcurve(color=color.blue)
def gforce(p1,p2):
    # Calculate the gravitational force exerted on p1 by p2.
    G = 1 # Change to 6.67e-11 to use real-world values.
    # Calculate distance vector between p1 and p2.
    r_vec = p1.pos-p2.pos
    # Calculate magnitude of distance vector.
    r_mag = mag(r_vec)
    # Calcualte unit vector of distance vector.
    r_hat = r_vec/r_mag
    # Calculate force magnitude.
    force_mag = G*p1.mass*p2.mass/r_mag**2
    # Calculate force vector.
    force_vec = -force_mag*r_hat
    
    return force_vec
    
star = sphere( pos=vector(-1,0,0),radius=0.05,
               mass = 2.0*100,
               momentum=vector(0,-500,0),
               texture = textures.stucco,
               make_trail=True )

planet = sphere( pos=vector(1,0,0),
                 spin=vector(0,0,1),
                 radius=0.05,
                 mass = 2.0*100,
                 texture = textures.earth,
                 momentum=vector(0,500,0),
                 make_trail=True )

dt = 0.0001
t = 0
while (True):
    rate(500)
    
    # Calculate forces.
    star.force = gforce(star,planet)
    planet.force = gforce(planet,star)
    # Update momenta.
    star.momentum = star.momentum + star.force*dt
    planet.momentum = planet.momentum + planet.force*dt
    # Update positions.
    star.pos = star.pos + star.momentum/star.mass*dt
    planet.pos = planet.pos + planet.momentum/planet.mass*dt
    t = t + dt


