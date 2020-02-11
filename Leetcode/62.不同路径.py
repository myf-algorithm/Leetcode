import math


def uniquePaths(self, m: int, n: int) -> int:
    return int(math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1))


def uniquePaths_dp(self, m: int, n: int) -> int:
    """
    dp[i][j]是到达i, j最多路径
    动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
    对于第一行dp[0][j]，或者第一列dp[i][0]，由于都是在边界，所以只能为1
    因为我们每次只需要dp[i-1][j], dp[i][j-1]
    """
    dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[-1][-1]


def uniquePaths_dp1(self, m: int, n: int) -> int:
    cur = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            cur[j] += cur[j - 1]
    return cur[-1]
