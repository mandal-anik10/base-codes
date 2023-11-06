# MODULE FOR LINEAR FITTING OF A SET OF DATA:


def Linearfit(x_data, y_Data):
    (sx, sy, p1, p2) = (0, 0, 0, 0)
    for i in range(len(x_data)):
        sx = sx + x_data[i]
        sy = sy + y_Data[i]
    xb = sx/len(x_data)
    yb = sy/len(y_Data)
    for i in range(len(x_data)):
        p1 = p1 + (x_data[i]-xb)*(y_Data[i]-yb)
        p2 = p2 + (x_data[i]-xb)**2
    m = p1/p2
    c = yb - m*xb
    return c,m

