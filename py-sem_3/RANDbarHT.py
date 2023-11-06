
# DETERMINATION OF THE BAR GRAPH OF THE NUMBER OF HEADS AND TAILS THROUGH RANDOM NUMBER GENERATION :


import random as rd
import matplotlib.pyplot as plt

i = 1
n = 10000

ctH = 0.0
ctT = 0.0

while i <= n:
    x = rd.random()

    if x < 0.5:
        ctH += 1.0
    else:
        ctT += 1.0

    i += 1

xx = [0.35, 0.65]
yy = [ctH, ctT]
zz = ["Head", "Tail"]

plt.bar(xx, yy, width=0.3, color=('r', 'g'))

plt.suptitle("DETERMINATION OF THE BAR GRAPH OF THE NUMBER OF HEADS AND TAILS THROUGH RANDOM NUMBER GENERATION")
plt.title("No. of Heads : "+str(ctH)+"    No. of Tails : "+str(ctT))
plt.xticks(xx, zz)
plt.xlim(-0.1, 1.1)
plt.ylim(0, n*0.6)
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.show()
