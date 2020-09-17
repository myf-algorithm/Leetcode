# _*_ encoding:utf-8 _*_
# 9.17依图笔试3
import sys

lines = sys.stdin.readline().strip()
N, K1, K2 = list(map(int, lines.split()))

lines = sys.stdin.readline().strip()
x, y, z = list(map(int, lines.split()))
Total = (x * 17 + y) * 29 + z

Values = []
for i in range(N):
    lines = sys.stdin.readline().strip()
    Values.append(list(map(int, lines.split())))

Nate = []
P = []
for i in range(N):
    xike = Values[i][0] * 17 + Values[i][1]
    nate = xike * 29 + Values[i][2]
    Nate.append(nate)
    P.append(Values[i][3])

Need = K1 - K2


# 花费
# 收益
# c为总钱数
# 在总钱数一定的情况下所能获得的最大收益
def pack1(w, v, c):
    # 它是先得到第一行的值，存到dp中，然后再直接用dp相当于就是上一行的值，所以下面必须用逆序
    # 否则dp[j-w[i-1]]可能会用到你本行的值，从大到小就不会
    dp = [0 for _ in range(c + 1)]
    for i in range(1, len(w) + 1):
        for j in reversed(range(1, c + 1)):  # 这里必须用逆序
            if w[i - 1] <= j:
                dp[j] = max(dp[j], dp[j - w[i - 1]] + v[i - 1])
    return dp[c]


if pack1(Nate, P, Total) < Need:
    print('NO')
else:
    print('YES')