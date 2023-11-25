# Determination of Principle axis of an inertia tensor and Angular momentum:

import scipy.linalg as al
from LocalModule.Matrix_Operation import *
from LocalModule.Inertia_Tensor import *

M = [2, 1, 4]
Pos = [[1, -1, 1], [2, 0, 2], [-1, 1, 0]]

I = Inertia_T(M, Pos)

evall, evec = al.eig(I)

eveci = al.inv(evec)

print("Principle axis vectors:\n", evec,)
print("And corresponding eigen values:\n", evall)

Id = M_Multiplication(M_Multiplication(eveci, I), evec)
print("Diagonalised Inertia Matrix:\n", Id)


omg = [[3], [-2], [4]]

L = M_Multiplication(I, omg)

print('Angular Momentum:\n', L)
