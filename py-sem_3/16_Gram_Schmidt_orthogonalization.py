'''
Gram-Schmidt Orthogonalization:

Author : Anik Mandal
'''
import numpy as np


def V_Dot(A, B):
    '''
    Performs Dot product between two vectors
    -----Inputs------------------------------------------
    A : ndarray
        First vector
    B : ndarray
        Second vector
    -----Output-------------------------------------------
    C : float
        Value of the dot product
    '''
    try:
        C = 0
        for i in range(len(A)):
            C = C + A[i][0] * B[i][0]
        return C
    except:
        ValueError('Dimension of A and B doesn\'t match')


def V_Mod(A):
    '''
    Calculates magnitude of a vector
    -----Inputs------------------------------------------
    A : ndarray
        Input vector
    -----Output-------------------------------------------
    Value of the magnitude of the vector
    '''
    return np.sqrt(V_Dot(A, A))


def V_Unit(A):
    '''
    Calculates Unit vector of a vector
    -----Inputs------------------------------------------
    A : ndarray
        Input vector
    -----Output-------------------------------------------
    C : ndarray
        Unit vector of the vector
    '''
    return A/V_Mod(A)

# Initial Vector set
A = np.array([[-1], [2], [3]])
B = np.array([[5], [-6], [7]])
C = np.array([[0], [4], [-8]])

# Orthogonalization:
UA = A
UB = B - (V_Dot(UA, B)/V_Mod(UA))*V_Unit(UA)
UC = C - (V_Dot(UA, C)/V_Mod(UA))*V_Unit(UA) - (V_Dot(UB, C)/V_Mod(UB))*V_Unit(UB)

nUA = V_Unit(UA)
nUB = V_Unit(UB)
nUC = V_Unit(UC)

print('New Ortho-Normal Vectors :')
print('New A : ', nUA)
print('New B : ', nUB)
print('New C : ', nUC)

print('\nCheck Orthogonality : \nDot of new_A and new_B', V_Dot(nUA,nUB))