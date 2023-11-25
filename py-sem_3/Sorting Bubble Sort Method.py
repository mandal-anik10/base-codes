
# SORTING A NUMERICAL LIST IN ASCENDING ORDER OR DESCENDING ORDER THROUGH BUBBLE SORT METHOD :

n = int(input('Number of elements in the list: ',))
xx = []
for i in range(n):
    x = float(input('Input elements: ',))
    xx.append(x)
print("My list :", xx)

for k in range(len(xx)-1):
    for i in range(0, len(xx)-1):
        if xx[i] < xx[i+1]:               # DESCENDING ORDER
            (xx[i], xx[i+1]) = (xx[i+1], xx[i])

print("My list after sorting in descending order : ", xx)
