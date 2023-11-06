
# SORTING A NUMERICAL LIST IN ASCENDING ORDER OR DESCENDING ORDER THROUGH INSERTION SORT METHOD :

n = int(input('Number of elements in the list: ',))
xx = []
for i in range(n):
    x = float(input('Input elements: ',))
    xx.append(x)
print("My list :", xx)

for i in range(1, len(xx)):
    for j in range(i, 0, -1):
        print(j)
        if xx[j - 1] > xx[i]:                   # Ascending order
            (xx[i], xx[j - 1]) = (xx[j - 1], xx[i])
            i = i - 1

print("Sorted list:", xx)
