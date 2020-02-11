class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        pp, p = 1, int(s[0] != '0')
        for i in range(1, len(s)):
            pp, p = p, pp * (9 < int(s[i - 1:i + 1]) <= 26) + p * (int(s[i]) > 0)
        return p

    def numDecodings_dp(self, s):
        dp = [0] * len(s)
        # 考虑第一个字母
        if s[0] == "0":
            return 0
        else:
            dp[0] = 1
        if len(s) == 1:
            return dp[-1]
        # 考虑第二个字母
        if s[1] != "0":
            dp[1] += 1
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, len(s)):
            # 当出现连续两个0
            if s[i - 1] + s[i] == "00":
                return 0
            # 考虑单个字母
            if s[i] != "0":
                dp[i] += dp[i - 1]
            # 考虑两个字母
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    S = Solution()
    print(S.numDecodings("12"))
