'''
#3: Determination of Principle axis of an inertia tensor and Angular momentum:

Author : Anik Mandal
'''
import scipy.linalg as al
import numpy as np

def Inertia_T(M, pos):
    '''
    This function calculates Inertia Tensor for a given discrete mass distribution
    -----Inputs-------------------------------------------------------------------
    M : list
        List of mass values
    pos : ndarray
        corrasponding positions of the masses
    -----Output--------------------------------------------------------------------
    I : ndarray
        Inertia Tensor of the mass distribution
    '''
    I = np.zeros((len(pos[0]), len(pos[0])))

    for m in range(len(pos[0])):
        for n in range(len(pos[0])):
            if m == n:
                for k in range(len(M)):
                    s = 0
                    for i in range(len(pos[0])):
                        if i != m:
                            s = s + M[k]*pos[k][i]**2
                            
                    I[m][n] = I[m][n] + s
                
            else:
                for k in range(len(M)):
                    s = - M[k]*pos[k][m]*pos[k][n]
                    
                    I[m][n] = I[m][n] + s
    return I

M = [2, 1, 4]
Pos = [[1, -1, 1], [2, 0, 2], [-1, 1, 0]]

I = Inertia_T(M, Pos)

evall, evec = al.eig(I)

eveci = al.inv(evec)

print("Principle axis vectors:\n", evec,)
print("And corresponding eigen values:\n", evall)

Id = np.matmul(np.matmul(eveci, I), evec)
print("Diagonalised Inertia Matrix:\n", Id)


omg = [[3], [-2], [4]]

L = np.matmul(I, omg)

print('Angular Momentum:\n', L)
