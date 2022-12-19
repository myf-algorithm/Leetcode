class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j]表示p的前i个字符和s的前j个字符是否匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 初始化
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # 状态更新
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':  # 【题目保证'*'号不会是第一个字符，所以此处有j>=2】
                    if s[i - 1] != p[j - 2] and p[j - 2] != '.':
                        dp[i][j] = dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2] | dp[i - 1][j]

        return dp[m][n]