# -*- coding:utf-8 -*-
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

class Solution:
    def rectCover(self, number):
        if number == 0 or number == 1 or number == 2:
            return number
        dp = [1, 2]
        for i in range(number - 2):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]


S = Solution()
print(S.rectCover(8))
