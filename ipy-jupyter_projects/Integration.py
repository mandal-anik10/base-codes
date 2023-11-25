
# INTEGRATION MODULE (SIMPSON'S 1-THIRD METHOD):


def Integrate(yy, xi, xf, n):
    h = (xf-xi)/(n-1)

    (i, s) = (1, 0)
    while i < (n-1):
        k = i % 2

        if k == 1:
            s = s+4*yy[i]
        else:
            s = s+2*yy[i]

        i = i+1

    s = (yy[0]+yy[n-1]+s)*h/3

    return s
