
def dist(Set_1,Set_2):
    s = 0
    for i in range(len(Set_2)):
        s = s+(Set_1[i]-Set_2[i])**2
    distance = s**(0.5)
    return (distance)