import turtle as tr

a = tr.Turtle()
a.speed(0)
a.lt(90)
a.penup()
a.backward(300)
a.pendown()
l = 0.80
r = 0.70
angle = 15

def tree(i):
    if i<10:
        while i<10 :
            break
    else:
        if i>100:
            a.pencolor('brown')
            a.pensize(i/15)
            a.fd(i)
            a.lt(angle)
            tree(i * l)
            a.rt(2*angle)
            tree(i * r)
            a.lt(angle)
            a.penup()
            a.backward(i)
            a.pendown()
        else:
            a.pencolor('green')
            a.pensize(i/15)
            a.fd(i)
            a.lt(angle)
            tree(i * l)
            a.rt(2*angle)
            tree(i * r)
            a.lt(angle)
            a.penup()
            a.backward(i)
            a.pendown()
tree(150)
tr.done()