n = int(input())
a = list(map(int, input().strip().split()))
res = a[0: len(a)]
for i in a:
    c = i
    while c > 1:
        if c % 2 == 0:
            c /= 2
        else:
            c = (3 * c + 1) / 2
        if c in res:
            res.remove(c)
res.sort(reverse=True)
if len(res) == 1:
    print(res[0], end='')
else:
    for i in range(len(res) - 1):
        print(res[i], end=' ')
    print(res[-1], end='')
