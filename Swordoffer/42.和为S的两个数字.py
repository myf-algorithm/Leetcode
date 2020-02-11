# -*- coding:utf-8 -*-
# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，
# 使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
# 对应每个测试案例，输出两个数，小的先输出。


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        memory = {}
        ret = []
        for num in array:
            if tsum - num in memory:
                if ret == []:
                    ret = [tsum - num, num]
                elif ret and ret[0] * ret[1] > (tsum - num) * num:
                    ret = [tsum - num, num]
            else:
                memory[num] = 1
        return ret


if __name__ == "__main__":
    S = Solution()
    print(S.FindNumbersWithSum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
