class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        动态规划：
        状态的定义为：以 s[i] 结尾的子字符串是否可以被空格拆分为一个或多个在字典中出现的单词。
        """
        size = len(s)
        assert size > 0
        word_set = {word for word in wordDict}  # 把wordDict放进一个哈希表中
        dp = [False for _ in range(size)]  # 这种状态定义很常见
        dp[0] = s[0] in word_set

        for r in range(1, size):  # r表示右边界
            if s[:r + 1] in word_set:
                dp[r] = True
                continue
            for l in range(r):  # l表示左边界
                if dp[l] and s[l + 1: r + 1] in word_set:
                    dp[r] = True  # 一旦得到dp[r] = True，break
                    break
        return dp[-1]

    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        动态规划：
        状态：dp[i]表示子串s[0:i]（即长度为i的子串，其实就是前缀）可以被空格拆分，
            并且拆分以后的单词是否落在 wordDict 中。这里 wordDict 要把它放入哈希表中，
            以快速判断一个单词是否在这个哈希表里。
        """
        size = len(s)
        assert size > 0
        word_set = {word for word in wordDict} # 预处理，把wordDict放进一个哈希表中
        # 状态定义：长度为 i 的子串可以被空格拆分为一个或多个在字典中出现的单词
        dp = [False for _ in range(size + 1)]
        dp[0] = True
        for r in range(1, size + 1):
            for l in range(r):
                # dp[l] 写在前面会更快一点，否则还要去切片，然后再放入 hash 表判重
                if dp[l] and s[l: r] in word_set:
                    dp[r] = True
                    break
        return dp[-1]
