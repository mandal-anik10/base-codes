
##SARC COV-2 STATISTICS:
'''''THE IDEA IS: CREATING INFECTION IN ONE PEOPLE AND DAY 1, THEN THE OTHER PEOPLE WITHIN UNSAFE DISTANCE WILL BE 
 INFECTED,AND IN THE NEXT DAY WHOLE POPULATION WILL BE SHIFTED TO A NEW LOCATION, OTHER PEOPLES WITHIN THE UNSAFE 
 DISTANCE FROM THE INFECTED PEOPLES WILL BE INFCTED AND THEN IT GOES ON AND ON'''''

from numpy import *
from random import *
from matplotlib.pyplot import *

xi = 0
xf = 10


#avg distance and total population:
n = 200                                 #population in one row
s = 0
for i in range(int(n)):
    s += 2*(n-i)
N = s-n                                 #total population
d = (xf-xi)/(n-1)                       #avg distance(useless)

xx = []                                 #to store x coordinate of people
yy = []                                 #to store y coordinate of people
val = []                                #to store health condition of people

time = linspace(1,30,30)



#creating initial position of people and first infection:
vic =randint(0,N)                       #first infection
for i in range(N):
    x = uniform(xi,xf)
    y = uniform(xi,xf)

    if i == vic:
        v = 0
    else:
        v = 1

    xx.append(x)
    yy.append(y)
    val.append(v)
plot(xx,yy,'.y')
infx = []
infy=[]
usd = d/10                              #unsafe distance
cc = []                                 #to store new infections per day
ct = []                                 #to store total infected people per day
Cti = 0                                 #count total infected people
tx = []
ty=[]
Ctl=[]
#creating infection:
for i in range(len(time)):
    Cpd =0                              #count per day
    for j in range(N):
        if val[j] ==0:
            infx.append(xx[j])
            infy.append(yy[j])
            Cpd = Cpd+1                 #counting
            k = 0
            ctl = 0
            while k < N and k!=j and val[k]!=0:
                ctl = ctl+1
                Ctl.append(ctl)
                if (xx[j]-xx[k])**2+(yy[j]-yy[k])**2<=10*usd**2:
                    val[k] = val[j]*val[k]           #transmission
                k = k+1
    # plot(time[i], xx[1])
    # print(time[i], yy[1])
    tx.append(xx[1])
    ty.append(yy[1])
    for l in range(N):                  #changing position
        x = uniform(xi, xf)
        y = uniform(xi, xf)
        xx[l] = x
        yy[l] = y

    Cti = Cti + Cpd                     # counting
    cc.append(Cpd)
    ct.append(Cti)

print(ctl,ct)                               #infected people per day
print(Ctl)
# plot(time,ct,'r')
plot(infx,infy,'.r')
show()
