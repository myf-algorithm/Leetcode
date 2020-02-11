n = int(input())
a = [int(i) for i in input().split()]
result = []
max = 0
for i in range(n):
    if a[i] > max:
        result.append(a[i])
        max = a[i]
    else:
        for j in range(len(result) - 1, -1, -1):
            if result[j] >= a[i]:
                del result[j]
            else:
                break
result.sort()
print(len(result))
if len(result) != 0:
    result = list(map(str, result))
    print(" ".join(result))
else:
    print("")
