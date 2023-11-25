from tkinter import *
import random as rd
import time
import numpy as np
tk = Tk()
canvas = Canvas(tk,width=5000,height=4000)
canvas.pack()
a= canvas.create_oval(500,500,510,510,fill='red')
x=np.linspace(-10*np.pi,10*np.pi, 10000)
y=np.linspace(-10*np.pi,10*np.pi, 10000)

b = []
for i in range(len(x)):
    s = np.sin(x[i])
    t = np.cos(y[i])
    canvas.move(a,s,t)
    if i>1:
        b.append(canvas.create_line(x[i-2],y[i-2],x[i-1],y[i-1], x[i], y[i], smooth = "true"))
    tk.update()
    time.sleep(0.00001)

tk.mainloop()
