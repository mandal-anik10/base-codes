# Crystal Structure(SC/BCC/FCC):

from vpython import *
from numpy import *
canvas(title='Crystal Structure', width=1500, height=700, background=color.black)
crystal = ['sc', 'bcc', 'fcc']

a = input("Type of Crystal (sc/bcc/fcc) : ")

if a == crystal[0]:
    canvas.title = 'Simple Cubic'
    for i in range(2):
        for j in range(2):
            for k in range(2):
                b = box(pos=vector(i - 0.5, j - 0.5, k - 0.5), length=1, height=1, width=1, opacity=0.15)
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                p = sphere(pos=vector(i, j, k), radius=0.02, color=color.cyan)

    for i in range(2):
        for j in range(2):
            for k in range(2):
                m = sphere(pos=vector(-i, -j, k), radius=0.5, color=color.red, opacity=0.2)
    print("Number of nearest neighbours : ", 6)

elif a == crystal[1]:
    canvas.title = 'Body Centered Cubic'
    for i in range(2):
        for j in range(2):
            for k in range(2):
                b = box(pos=vector(i - 0.5, j - 0.5, k - 0.5), length=1, height=1, width=1, opacity=0.15)
                p = sphere(pos=vector(i-0.5, j-0.5, k-0.5), radius=0.02, color=color.cyan)
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                p = sphere(pos=vector(i, j, k), radius=0.02, color=color.cyan)

    bcm = sphere(pos=vector(-0.5, -0.5, 0.5), radius=(3**0.5)/4, color=color.red, opacity=0.15)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                m = sphere(pos=vector(-i, -j, k), radius=(3**0.5)/4, color=color.red, opacity=0.15)
    print("Number of nearest neighbours : ", 8)

else:
    canvas.title = 'Face Centered Cubic'
    for i in range(2):
        for j in range(2):
            for k in range(2):
                b = box(pos=vector(i - 0.5, j - 0.5, k - 0.5), length=1, height=1, width=1, opacity=0.15)
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                pc = sphere(pos=vector(i, j, k), radius=0.02, color=color.cyan)
    for i in range(-2, 3):
        for j in range(-2, 3):
            for k in range(-2, 3):
                if (abs(i) % 2 and abs(j) % 2 == 1 and abs(k) % 2 == 0) or (abs(j) % 2 and abs(k) % 2 == 1 and abs(i) % 2 == 0) or (abs(i) % 2 and abs(k) % 2 == 1 and abs(j) % 2 == 0):
                    ps = sphere(pos=vector(i/2, j/2, k/2), radius=0.02, color=color.cyan)

    for i in range(2):
        for j in range(2):
            for k in range(2):
                m = sphere(pos=vector(-i, -j, k), radius=1/(2*2**0.5), color=color.red, opacity=0.15)
    sphere(pos=vector(0, -0.5, 0.5), radius=1 / (2 * 2 ** 0.5), color=color.red, opacity=0.15)
    sphere(pos=vector(-0.5, -0.5, 0), radius=1 / (2 * 2 ** 0.5), color=color.red, opacity=0.15)
    sphere(pos=vector(-0.5, 0, 0.5), radius=1 / (2 * 2 ** 0.5), color=color.red, opacity=0.15)
    sphere(pos=vector(-1, -0.5, 0.5), radius=1 / (2 * 2 ** 0.5), color=color.red, opacity=0.15)
    sphere(pos=vector(-0.5, -0.5, 1), radius=1 / (2 * 2 ** 0.5), color=color.red, opacity=0.15)
    sphere(pos=vector(-0.5, -1, 0.5), radius=1 / (2 * 2 ** 0.5), color=color.red, opacity=0.15)
    print("Number of nearest neighbours : ", 12)

