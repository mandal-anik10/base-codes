Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import turtle as tr
>>> 
>>> a = tr.Turtle()
>>> 
>>> a.penup()
>>> a.goto(-128,-128)
>>> a.pendown()
>>> 
>>> cc = []
>>> c1 = []
>>> c2 = []
>>> 
>>> for i in range (4):
	cc.append(a.pos())
	a.fd(256)
	a.lt(90)

	
>>> for i in range(2,4):
	a.penup()
	a.goto(cc[i])
	a.pendown()
	