def minimumDeleteSum(self, s1: str, s2: str) -> int:
    def lcs(text1, text2):
        len1 = len(text1)
        len2 = len(text2)
        # dp[i][j]为 s1[i..] 和 s2[j..] 的最长公共子序列长度
        dp = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
        for i in range(1, len2 + 1):
            for j in range(1, len1 + 1):
                if text2[i - 1] == text1[j - 1]:
                    # text1[i-1] 和 text2[j-1] 必然在 lcs 中
                    dp[i][j] = dp[i - 1][j - 1] + ord(text2[i - 1])
                else:
                    # text1[i-1] 和 text2[j-1] 至少有一个不在 lcs 中
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    ascSum = 0
    ascSum += sum([ord(char) for char in list(s1)])
    ascSum += sum([ord(char) for char in list(s2)])

    return ascSum - 2 * lcs(s1, s2)