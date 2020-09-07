# 找缺失数字
# @param a int整型一维数组 给定的数字串
# @return int整型

class Solution:
    def solve(self, a):
        # write code here
        if len(a) == 0:
            return 0
        if a[0] == 1:
            return 0
        for i in range(1, len(a)):
            if a[i - 1] + 1 != a[i]:
                return a[i - 1] + 1
