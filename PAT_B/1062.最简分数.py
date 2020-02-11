a, b, c = input().split()
n1, m1 = map(float, a.split('/'))
n2, m2 = map(float, b.split('/'))
c = int(c)
x, y = n1 / m1, n2 / m2
min_, max_ = min(x, y), max(x, y)


def judge(a, b):
    while b:
        c = a % b
        a, b = b, c
    if a == 1:
        return False
    else:
        return True


f = 0
for i in range(1, c):
    val = float(i) / c
    if val >= max_:
        break
    if val > min_:
        if judge(i, c):
            continue
        if f == 0:
            print("%d/%d" % (i, c), end="")
            f = 1
        else:
            print(" %d/%d" % (i, c), end="")
