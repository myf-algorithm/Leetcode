def putApple(m, n):
    if m == 0 or n == 1:
        return 1
    if n > m:
        return putApple(m, m)
    else:
        return putApple(m, n - 1) + putApple(m - n, n)


while True:
    try:
        n, m = map(int, input().split())
        print(putApple(n, m))
    except:
        break
