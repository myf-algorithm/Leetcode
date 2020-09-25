# encoding:utf-8
# 9.25 搜狗笔试3
#
#
#
#
# @param n int整型 初始球数
# @return double浮点型
#
class Solution:
    def calcProb(self, n):
        # write code here
        if n == 1 or n == 2 or n == 3:
            return 1
        elif n == 4 or n == 5 or n == 6:
            return 0.5
        else:
            return 0.5
