
# SUMMATION MODULE:


def Summation(yy, xi, xf, step):

    (s, i) = (0, xi)

    while i <= xf:
        s = s+yy[i]
        i = i+step

    return s
