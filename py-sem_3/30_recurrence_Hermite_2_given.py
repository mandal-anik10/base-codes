'''
Recurrence Hermite(2 Given):

Author : Anik Mandal
'''
import matplotlib.pyplot as plt
import numpy as np

# h1x = 2*x
# h0x = 1


xx = np.linspace(0,2,1000)

h1x = []
h0x = []

h2x = []
for i in range(len(xx)):
    h0 = 1
    h1 = 2*xx[i]

    h2 = 2*xx[i]*h1 - 2*1*h0

    h0x.append(h0)
    h1x.append(h1)
    h2x.append(h2)

plt.plot(xx,h0x,'k',xx,h1x,'g',xx,h2x,'r')
plt.legend(['$Hermite Polynomial$ of Degree 0(Given)','$Hermite Polynomial$ of Degree 1(Given)','$Hermite Polynomial$ of Degree 2(Determined)'])
plt.xlabel('x')
plt.ylabel('Value of the Hermite terms')
plt.grid()
plt.show()