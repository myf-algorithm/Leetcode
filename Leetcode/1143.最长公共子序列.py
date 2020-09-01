class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        res = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
        for i in range(1, len2 + 1):
            for j in range(1, len1 + 1):
                if text2[i - 1] == text1[j - 1]:
                    res[i][j] = res[i - 1][j - 1] + 1
                else:
                    res[i][j] = max(res[i - 1][j], res[i][j - 1])
        return res[-1][-1]


class Solution1:
    def LCS(self, list_n, list_m):
        n = len(list_n)
        m = len(list_m)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if list_n[i - 1] == list_m[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if dp[-1][-1] == 0:
            return -1
        list_LCS = []
        i, j = n, m
        while i > 0 and j > 0:
            if list_n[i - 1] == list_m[j - 1]:
                list_LCS.append(list_n[i - 1])
                i -= 1
                j -= 1
                continue
            else:
                if dp[i][j - 1] >= dp[i - 1][j]:
                    j -= 1
                else:
                    i -= 1
        return ''.join(list(reversed(list_LCS)))


S = Solution1()
print(S.LCS("1A2C3D4B56", "B1D23CA45B6A"))
