# 动态规划解法
def uniquePath(m, n):
    if m == 1 or n == 1:
        return 1
    result = [[0 for i in range(n)]] * m
    for i in range(m):
        result[i][0] = 1
    for i in range(n):
        result[0][i] = 1
    for i in range(1, m):
        for j in range(1, n):
            result[i][j] = result[i - 1][j] + result[i][j - 1]
    return result[m - 1][n - 1]


while True:
    try:
        print(uniquePath(*map(lambda c: int(c) + 1, input().split())))
    except:
        break

# 递归解法
while True:
    try:
        n, m = list(map(int, input().split(' ')))


        def road(x, y):
            if x == 0 or y == 0:
                return 1
            else:
                return road(x - 1, y) + road(x, y - 1)


        result = road(n, m)
        print(result)
    except:
        break
