# -*- coding:utf-8 -*-
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

class Solution:
    def NumberOf1(self, n):
        return bin(n & 0xffffffff).count('1')


S = Solution()
print(S.NumberOf1(100))
