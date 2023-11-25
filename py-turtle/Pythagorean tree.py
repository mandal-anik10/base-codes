import turtle as tr

a = tr.Turtle()
a.speed(0)

a.penup()
a.goto(-64,-300)
a.pendown()


def tree(i):
    if i<10:
        while i<10 :
            break
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
        tree(i/2**0.5)
        a.rt(135)
        a.penup()
        for j in range(3):
            a.fd(i)
            a.lt(90)
        a.rt(45)
        a.fd(i/2**0.5)
        a.pendown()
        a.lt(180)
        tree(i/2**0.5)
        a.penup()
        a.fd(i / 2 ** 0.5)
        a.rt(135)
        for j in range(2):
            a.fd(i)
            a.lt(90)
        a.pendown()

a.fillcolor('indigo')
a.begin_fill()
tree(128)
a.end_fill()

tr.done()
