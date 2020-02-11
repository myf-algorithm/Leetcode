# -*- coding:utf-8 -*-
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

class Solution:
    def jumpFloor(self, number):
        if number == 1 or number == 2:
            return number
        ret = sum_ = 3
        for i in range(number - 2):
            ret = sum_ + 1
            sum_ += ret
        return ret


S = Solution()
print(S.jumpFloor(3))
