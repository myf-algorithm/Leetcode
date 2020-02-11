def f(n, x):
    res = ""
    while True:
        res += str(n % x)
        n = n // x
        if n == 0:
            break
    return res


a, b, x = list(map(int, input().strip().split()))
print(f(a + b, x)[::-1])
