'''
#1: Determination of Inertia Tensor:

Author : Anik Mandal
'''

import numpy as np

M = [1, 1, 1, 1]
pos = [[1, 1, 0], [1, -1, 0], [-1, 1, 0], [-1, -1, 0]]

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

print(I)
