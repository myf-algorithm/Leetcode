a = list(map(str, input()))
for i in range(len(a)):
    if 'A' <= a[i] <= 'Z':
        a[i] = a[i].lower()
count = {}
for i in a:
    if 'a' <= i <= 'z':
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
count_st = sorted(count.items(), key=lambda a: (-a[1], a[0]))
print(count_st[0][0], count_st[0][1])
