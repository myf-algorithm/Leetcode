# 先用2去筛，即把2留下，把2的倍数剔除掉；
# 再用下一个素数，也就是3筛，把3留下，把3的倍数剔除掉；
# 接下去用下一个素数5筛，把5留下，把5的倍数剔除掉；
# 不断重复下去

def prime_eratosthenes(n):
    prime = []
    flag = [1] * (n + 2)
    p = 2
    while p <= n:
        prime.append(p)
        for i in range(2 * p, n + 1, p):
            flag[i] = 0
        while 1:
            p += 1
            if flag[p] == 1:
                break
    return prime


import math

def prime(n):
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    if n % 5 == 0:
        return n == 5
    for p in range(7, int(math.sqrt(n)) + 1, 2):  # 只考虑奇数作为可能因子
        if n % p == 0:
            return 0
    return 1


N = int(input())
count = 0
prime_num = []
# prime_num = prime_eratosthenes(N)
for i in range(2, N + 1):
    if prime(i):
        prime_num.append(i)
for i in range(len(prime_num) - 1):
    if prime_num[i + 1] - prime_num[i] == 2:
        count += 1
print(count)
