'''
DETERMINATION OF THE VALUE OF nCr AND nPr :

Author : Anik Mandal
'''

n = 7
r = 0

while r <= n:
    (fn, fr, fnr) = (1, 1, 1)

    for i in range(1, n+1, 1):
        fn = fn*i

    for j in range(1, r+1, 1):
        fr = fr*j

    for k in range(1, n-r+1, 1):
        fnr = fnr*k

    nCr = fn/(fr*fnr)
    nPr = fn/fnr

    print("nCr for n:", n, "r :", r, " equals to :", nCr)
    print("npr for n:", n, "r :", r, " equals to :", nPr)
    r = r+1
