# -*- coding:utf-8 -*-
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

# f[n] = f[n-1] + f[n-2]


class Solution:
    def jumpFloor(self, number):
        if number == 1 or number == 2:
            return number
        dp = [1, 2]
        for i in range(number - 2):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]


S = Solution()
print(S.jumpFloor(50))
