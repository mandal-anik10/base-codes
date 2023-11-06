# ARRAY OR MATRIX OPERATIONS :

import numpy as np

xx = [[1.0, 2.0, 3.0], [-5.0, 0.0, 5.0], [0.0, -1.0, 1.0]]
yy = [[0.0, 5.0, 10.0], [1.0, 2.0, 3.0], [-1.0, 0.0, 1.0]]

print("My matrices are \nxx :", xx, "\nyy :", yy)

addxy = np.zeros((3, 3))
sbtxy = np.zeros((3, 3))
mltxy = np.zeros((3, 3))
trsx = np.zeros((3, 3))

trx = 0.0

for i in range(3):
    for j in range(3):
        addxy[i][j] = xx[i][j] + yy[i][j]
        sbtxy[i][j] = xx[i][j] - yy[i][j]

        for k in range(3):
            mltxy[i][j] += xx[i][k] * yy[k][j]

        trsx[j][i] = xx[i][j]

    trx += xx[i][i]

print("The addition of xx and yy matrix is : \n", addxy)
print("The substraction of xx from yy matrix is : \n", sbtxy)
print("The multiplication of xx to yy matrix is : \n", mltxy)
print("The transpose of xx matrix is : \n", trsx)
print("The tr(xx) : ", trx)
