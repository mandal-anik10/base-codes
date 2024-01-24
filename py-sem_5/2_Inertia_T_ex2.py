'''
#2: Determination of inertia tensor: 

Author : Anik Mandal
'''

import numpy as np

M = [1, 0.5, 2]
pos = [[1, 0, 0], [0, 1, 2], [0, 2, 1]]


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


IT = Inertia_T(M, pos)

print(IT)
