class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)  # 表示s的前i位能否用worddict中的单词表示
        dp[0] = True
        for i in range(n):  # i表示开始索引
            for j in range(i + 1, n + 1):  # j表示结束索引
                if (dp[i] and (s[i:j] in wordDict)):
                    dp[j] = True
        return dp[-1]
