#prime number(r,theta) plot:
	
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,7))

maxn=2500
r=np.linspace(0,maxn,maxn+1)
rr=[1,2]

for i in range(3,len(r)):
	m=1
	for j in range(2,i):
		k=i%j
		m=m*k
	if m!=0:
		rr.append(i)
xx=[]
yy=[]
for i in range(len(rr)):
	x=rr[i]*np.cos(rr[i])
	y=rr[i]*np.sin(rr[i])
	
	xx.append(x)
	yy.append(y)

plt.plot(xx,yy,'.r')

plt.title("(r,θ) plot of Prime numbers as (n,n)   max number ="+str(maxn))
plt.xlabel("x Axis")
plt.ylabel("y Axis")
plt.grid()
plt.show()

