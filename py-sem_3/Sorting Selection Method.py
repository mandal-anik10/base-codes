
# SORTING A NUMERICAL LIST IN ASCENDING ORDER OR DESCENDING ORDER THROUGH SELECTION SORT METHOD :

n = int(input('Number of elements in the list: ',))
xx = []
for i in range(n):
    x = float(input('Input elements: ',))
    xx.append(x)
print("My list :", xx)

for i in range(0, len(xx)):
    for j in range(i+1, len(xx)):
        if xx[i] > xx[j]:               # ASCENDING ORDER
            (xx[i], xx[j]) = (xx[j], xx[i])

print("My list after sorting in ascending order : ", xx)
