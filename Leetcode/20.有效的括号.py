class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            elif i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0


if __name__ == '__main__':
    S = Solution()
    nums = "(])"
    print(S.isValid(nums))
