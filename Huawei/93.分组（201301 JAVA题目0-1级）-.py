def dfs(i, n, a, res, s):
    if i == n:
        return abs(res) == s
    else:
        return dfs(i + 1, n, a, res + a[i], s) or dfs(i + 1, n, a, res - a[i], s)


try:
    while True:
        n = input()
        n = int(n)
        l = list(map(int, input().split()))
        s1, s2 = 0, 0
        num = []
        for i in range(n):
            if l[i] % 5 == 0:
                s1 += l[i]
            elif l[i] % 3 == 0:
                s2 += l[i]
            else:
                num.append(l[i])
        d = abs(s1 - s2)
        if dfs(0, len(num), num, 0, d):
            print('true')
        else:
            print('false')
except:
    pass
