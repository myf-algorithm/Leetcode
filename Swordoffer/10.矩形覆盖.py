# -*- coding:utf-8 -*-
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

# 对于矩形的覆盖，可以考虑最后的覆盖是横着还是竖着的小矩形
# 如果是竖着(占一列)，则有 f(n‐1)种覆盖方法
# 如果是横着(占两行)，则有 f(n‐2)种覆盖方法
# 因此一共有 f(n) = f(n‐1) + f(n‐2)种覆盖方法


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
