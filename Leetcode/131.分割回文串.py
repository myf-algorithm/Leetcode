class Solution(object):
    def partition_traceback(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def helper(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])

        helper(s, [])
        return res

    def partition_dp_dfs(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
        res = []

        def helper(i, tmp):
            if i == n:
                res.append(tmp)
            for j in range(i, n):
                if dp[i][j]:
                    helper(j + 1, tmp + [s[i: j + 1]])

        helper(0, [])
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.partition_traceback("aab"))
