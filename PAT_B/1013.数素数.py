import math


def prime(n):
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    if n % 5 == 0:
        return n == 5
    for p in range(7, int(math.sqrt(n)) + 1, 2):
        if n % p == 0:
            return 0
    return 1


def prime_list(n):
    count = 0
    cur = 2
    res = []
    while count < n:
        if prime(cur):
            count += 1
            res.append(cur)
        cur += 1
    return res


a = [int(i) for i in input().strip().split()]
M, N = a[0], a[1]
res = prime_list(N)[M - 1:]
for i in range(len(res)):
    if i % 10 == 9:
        print(res[i])
    else:
        if i == len(res) - 1:
            print(res[i])
        else:
            print(res[i], end=' ')

