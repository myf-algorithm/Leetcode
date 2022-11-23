# Python3 模拟，字典统计每个字符个数，使用栈进行保存结果
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = Counter(s)
        stack = [s[0]]
        dic[s[0]] -= 1
        for i in range(1, len(s)):
            while stack and stack[-1] > s[i] and dic[stack[-1]] > 0 and s[i] not in stack:
                stack.pop()
            if s[i] not in stack:
                stack.append(s[i])
            dic[s[i]] -= 1
        return "".join(stack)
