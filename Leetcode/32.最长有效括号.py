class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        n = len(s)
        dp = [0] * n
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                if s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                res = max(res, dp[i])
        return res


class Solution_Stack(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res


class Solution1:
    def longestValidParentheses(self, s):
        res = 0
        stack = []
        prev = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i - prev)
                prev = 0
            else:
                if len(stack) > 0:
                    prev = i - stack.pop() + 1
                    res = max(res, prev)
                else:
                    prev = 0
        return res
