import numpy as np
import time as t

A = np.random.randint(-1000, 1000, 1000)
B = np.random.randint(-1000, 1000, 1000)
S = A + B

tsi = t.time()
S.sort()
tsf = t.time()
print("Time for Whole Sorting:", tsf-tsi)


tci = t.time()
A.sort()
B.sort()
C = []

count = 0

for i in range(len(A)):
    for j in range(count, len(B)):
        if A[i] > B[j]:
            C.append(B[j])
            count = count + 1
        else:
            C.append(A[i])
            break
        if j == len(B) - 1:
            for k in range(i, len(A)):
                C.append(A[k])
    if i == len(A) - 1:
        for k in range(count, len(B)):
            C.append(B[k])

tcf = t.time()
print("Time in our method:", tcf-tci)
print(S, "\n", C)



