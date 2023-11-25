#

from vpython import *
canvas(height = 750, width = 1500)


def Central_F(on_o,due_to_o):
    k = 1
    r_vec = on_o.pos-due_to_o.pos
    r_mag = mag(r_vec)
    r_cap = r_vec/r_mag
    f_mag = k*(on_o.charge)*(due_to_o.charge)/r_mag**2
    f_vec = f_mag*r_cap
    return f_vec


electron = sphere(pos = vector(-10,0,0),
                  radius = 0.2,
                  charge = -10,
                  mass = 1,
                  momentum = vector(0,-1,0),
                  color = color.red,
                  make_trail=True)
positron = sphere(pos = vector(10,0,0),
                  radius = 0.2,
                  charge = 10,
                  mass = 1,
                  momentum = vector(0,1,0),
                  color = color.blue,
                  make_trail=True)

e_axis = arrow(pos = vector(0,0,0),
               axis = electron.pos,
               shaftwidth=0.05,
               headwidth=0.1
               )
p_axis = arrow(pos = vector(0,0,0),
               axis = positron.pos,
               shaftwidth=0.05,
               headwidth=0.1
               )

e_l = label(pos = electron.pos,
            text = 'electron',
            yoffset = 25
            )
p_l = label(pos = positron.pos,
            text = 'positron',
            yoffset = 25
            )
v_l = label(pos = 0.5*e_axis.pos,
            text = 'vibrational axis',
            yoffset = 25
            )

dt = 0.001
t =0

while(True):
    rate(2000)
    
    electron.force = Central_F(electron,positron)
    positron.force = Central_F(positron,electron)

    electron.momentum = electron.momentum + electron.force*dt
    positron.momentum = positron.momentum + positron.force*dt

    electron.pos = electron.pos + electron.momentum*dt/electron.mass
    positron.pos = positron.pos + positron.momentum*dt/positron.mass

    e_axis.axis = electron.pos
    p_axis.axis = positron.pos

    e_l.pos = electron.pos
    p_l.pos = positron.pos
    v_l.pos = 0.5*e_axis.pos
    
    t = t + dt

    
    
