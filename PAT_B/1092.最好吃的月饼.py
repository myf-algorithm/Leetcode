n = list(map(int, input().split(' ')))
l = [0 for i in range(n[0])]
o = []
for i in range(n[1]):
    ll = list(map(int, input().split(' ')))
    l = [l[j] + ll[j] for j in range(n[0])]
ml = max(l)
print(ml)
for i in range(n[0]):
    if l[i] == ml:
        o.append(str(i + 1))
print(' '.join(o))
