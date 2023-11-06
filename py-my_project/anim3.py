from vpython import *
import random as rd

canvas(title='Random motion in 3D',
       width=750, height=500, center=vector(0, 0, 0),
       background=color.white)

(xi, yi, zi) = (0, 0, 0)
r0 = vector(xi, yi, zi)
p = sphere(pos=r0, radius=0.5, color=color.cyan)
trail = curve(color=color.red)

for i in range(50):
    xf = 10*rd.uniform(-1, 1)
    yf = 10*rd.uniform(-1, 1)
    zf = 10*rd.uniform(-1, 1)

    vel = 10
    r = vector(xf, yf, zf)
    d = ((xf-xi)**2+(yf-yi)**2+(zf-zi)**2)**0.5
    tp = d/vel
    t = 0
    while t <= tp:
        rate(200)

        trail.append(pos=p.pos)
        p.pos = (r/tp)*t + r0
        t = t+0.01

    r0 = r
    p.pos = r0
    sphere(pos=p.pos, radius=0.2, color=color.black)
    (xi, yi, zi) = (xf, yf, zf)



