# -*- coding:utf-8 -*-
# 大家都知道斐波那契数列，现在要求输入一个整数n，
# 请你输出斐波那契数列的第n项（从0开始，第0项为0）


class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        memories = [1, 1]
        for i in range(n - 2):
            memories.append(memories[-1] + memories[-2])
        return memories[-1]


S = Solution()
print(S.Fibonacci(50))
