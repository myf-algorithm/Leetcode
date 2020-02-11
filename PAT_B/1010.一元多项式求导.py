num = [int(i) for i in input().strip().split()]
res = []
for i in range(0, len(num), 2):
    if num[i + 1] > 0:
        res.append(num[i] * num[i + 1])
        res.append(num[i + 1] - 1)
if len(res) >= 2:
    for i in range(len(res) - 1):
        print(res[i], end=' ')
    print(res[-1], end='')
else:
    print(0, end=' ')
    print(0, end='')