class Solution(object):
    def isMatch(self, s, p):
        """
        动态规划
        """
        sn = len(s)
        pn = len(p)
        dp = [[False] * (pn + 1) for _ in range(sn + 1)]
        dp[0][0] = True
        for j in range(1, pn + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]
        for i in range(1, sn + 1):
            for j in range(1, pn + 1):
                if (s[i - 1] == p[j - 1] or p[j - 1] == "?"):
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]

    def isMatch1(self, s, p):
        """
        双指针法
        """
        i = 0
        j = 0
        start = -1
        match = 0
        while i < len(s):
            # 一对一匹配,匹配成功一起移
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            # 记录p的"*"的位置,还有s的位置
            elif j < len(p) and p[j] == "*":
                start = j
                match = i
                j += 1
            # j 回到 记录的下一个位置
            # match 更新下一个位置
            # 这不代表用*匹配一个字符
            elif start != -1:
                j = start + 1
                match += 1
                i = match
            else:
                return False
        # 将多余的 * 直接匹配空串
        return all(x == "*" for x in p[j:])


if __name__ == '__main__':
    S = Solution()
    s = "adceb"
    p = "*a*b"
    print(S.isMatch(s, p))
