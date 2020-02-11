n = input()
m = list(map(int, input().split()))
m.sort()
a = m[0] / 2 + m[1] / 2
for i in m[2:]:
    a = a / 2 + i / 2
print(int(a))
