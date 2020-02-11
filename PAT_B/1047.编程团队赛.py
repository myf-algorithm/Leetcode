N = int(input())
s = {}
for _ in range(N):
    a = list(map(str, input().strip().split()))
    score = int(a[1])
    name = list(map(int, a[0].strip().split('-')))[0]
    if name not in s:
        s[name] = score
    else:
        s[name] += score
res = max(zip(s.values(), s.keys()))
print(res[1], res[0])
