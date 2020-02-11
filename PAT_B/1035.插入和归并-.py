def Isort(n, m):
    x = 0
    for i in range(1, len(n)):
        k = n[:i + 1]
        k.sort()
        k.extend(n[i + 1:])
        if x == 1:
            return k
        if k == m:
            x = 1
    return False


def Msort(n, m):
    x = 0
    n = [[i] for i in n]
    while len(n) > 1:
        k = []
        for j in range(0, len(n), 2):
            try:
                n[j].extend(n[j + 1])
                k.append(n[j])
            except:
                k.append(n[j])
        for i in k:
            i = i.sort()
        n = k[:]
        result = []
        for i in k:
            for l in i:
                result.append(l)
        if x == 1:
            return result
        if result == m:
            x = 1


n = input()
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a1 = a[:]
m = Isort(a, b)
if m != False:
    print("Insertion Sort")
    for i in range(len(m) - 1):
        print(m[i], end=" ")
    print(m[i + 1], end="")
else:
    m = Msort(a1, b)
    print("Merge Sort")
    for i in range(len(m) - 1):
        print(m[i], end=" ")
    print(m[i + 1], end="")
