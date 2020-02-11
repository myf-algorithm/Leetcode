a = input().split()
m = 0
n = 0
for i in range(int(a[0])):
    b = input().split()
    x = 0
    for j in range(1, len(b)):
        if float(b[j]) < float(a[1]):
            x += 1
    if x > int(b[0]) // 2:
        m += 1
        if int(b[0]) > int(a[2]):
            n += 1
            m -= 1

m = m / int(a[0]) * 100
n = n / int(a[0]) * 100
m = '%.1f' % m
n = '%.1f' % n
print("%s%c%c%s%c" % (m, '%', ' ', n, '%'), end="")
