# -*- coding:utf-8 -*-
# 一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级......它也可以跳上 n 级。求
# 该青蛙跳上一个 n 级的台阶总共有多少种跳法

# f(n) = f(n - 1)+ f(n - 2) + f(n - 3) + ... + f(1)
# f(n) = 2 * f(n - 1)


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
