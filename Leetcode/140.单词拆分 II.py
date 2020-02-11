class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        from collections import deque
        size = len(s)
        assert size > 0
        word_set = {word for word in wordDict}
        dp = [False for _ in range(size)]
        dp[0] = s[0] in word_set
        for r in range(1, size):
            if s[:r + 1] in word_set:
                dp[r] = True
                continue
            for l in range(r):
                if dp[l] and s[l + 1: r + 1] in word_set:
                    dp[r] = True
                    break
        res = []
        if dp[-1]:
            queue = deque()
            self.__dfs(s, size - 1, wordDict, res, queue, dp)
        return res

    def __dfs(self, s, end, word_set, res, path, dp):
        # print('刚开始', s[:end + 1])
        # 如果不用拆分，整个单词就在word_set中就可以结算了
        if s[:end + 1] in word_set:
            path.appendleft(s[:end + 1])
            res.append(' '.join(path))
            path.popleft()

        for i in range(end):
            if dp[i]:
                suffix = s[i + 1:end + 1]
                if suffix in word_set:
                    path.appendleft(suffix)
                    self.__dfs(s, i, word_set, res, path, dp)
                    path.popleft()
