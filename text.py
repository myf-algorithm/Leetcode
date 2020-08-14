a = [1, 2, 3, 4, 5, 6, 7, 1, 1, 3, 4, 4]
for i in range(len(a)):
    temp = []
    for j in range(len(a)):
        temp.append(a[j] - a[i])
    print(temp)
