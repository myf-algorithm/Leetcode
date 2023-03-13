# -*- coding:utf-8 -*-
# 请实现一个函数用来匹配包括'.'和'*'的正则表达式。
# 模式中的字符'.'表示任意一个字符，
# 而'*'表示它前面的字符可以出现任意次（包含0次）。
# 在本题中，匹配是指字符串的所有字符匹配整个模式。
# 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，
# 但是与"aa.a"和"ab*a"均不匹配

import re


class Solution_re:
    def isMatch(self, s: str, p: str) -> bool:
        ans = re.fullmatch(p, s)
        return ans != None


class Solution_dic:
    # s, pattern都是字符串
    def __init__(self):
        self.dic = {}

    def match(self, s, p):
        if (s, p) in self.dic:
            return self.dic[(s, p)]
        if p == '':
            return s == ''
        if len(p) == 1 or p[1] != '*':
            self.dic[(s[1:], p[1:])] = self.match(s[1:], p[1:])
            return len(s) > 0 and (p[0] == '.' or p[0] == s[0]) and self.dic[(s[1:], p[1:])]
        while len(s) and (p[0] == '.' or p[0] == s[0]):
            self.dic[(s, p[2:])] = self.match(s, p[2:])
            if self.match(s[:], p[2:]):
                return True
            s = s[1:]
        self.dic[(s, p[2:])] = self.match(s, p[2:])
        return self.dic[(s, p[2:])]


class Solution_dp:
    def isMatch(self, s, p):
        if not s and not p:
            return True
        if (s and not p) or (not s and p and p != '*'):
            return False
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(p) + 1):
            if dp[0][i - 1]:
                if p[i - 1] == '*':
                    dp[0][i] = True
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1] or dp[i - 1][j]
        return dp[len(s)][len(p)]


if __name__ == '__main__':
    S = Solution_dp()
    print(S.isMatch('aaa', 'a*a'))
