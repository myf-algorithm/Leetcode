import math


# 点号可以匹配任意一个字符
# 星号通配符可以让前一个字符重复任意次数，包括零次。
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        return first_match and self.isMatch(s[1:], p[1:])

    def isMatch_DP(self, s: str, p: str) -> bool:
        def dp(i, j):
            memo = dict()  # 备忘录
            if (i, j) in memo: return memo[(i, j)]
            if j == len(p): return i == len(s)
            first = i < len(s) and p[j] in {s[i], '.'}
            if j <= len(p) - 2 and p[j + 1] == '*':
                ans = dp(i, j + 2) or first and dp(i + 1, j)
            else:
                ans = first and dp(i + 1, j + 1)
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)


if __name__ == '__main__':
    S = Solution()
    s = "aa"
    p = "a*"
    print(S.isMatch_DP(s, p))
