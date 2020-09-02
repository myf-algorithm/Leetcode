class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        # (n1 + 1)行，(n2 + 1)列
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] + 1
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # word1 为 "horse"，word2 为 "ros"
                    # dp[i - 1][j - 1]到dp[i][j]需要替换操作
                    # dp[i - 1][j]到dp[i][j]需要表示删除操作
                    # dp[i][j - 1]到dp[i][j]需要表示插入操作
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]


class Solution1:
    def minEditCost(self, str1, str2, ic, dc, rc):
        n1 = len(str1)
        n2 = len(str2)
        # (n1 + 1)行，(n2 + 1)列
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] + ic
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + dc
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # word1 为 "horse"，word2 为 "ros"
                    # dp[i - 1][j - 1]到dp[i][j]需要替换操作
                    # dp[i - 1][j]到dp[i][j]需要表示删除操作
                    # dp[i][j - 1]到dp[i][j]需要表示插入操作
                    dp[i][j] = min(dp[i][j - 1] + ic, dp[i - 1][j] + dc, dp[i - 1][j - 1] + rc)
        return dp[-1][-1]
