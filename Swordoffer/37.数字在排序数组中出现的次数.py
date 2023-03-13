# -*- coding:utf-8 -*-
# 统计一个数字在排序数组中出现的次数。


class Solution:
    def GetNumberOfK(self, data, k):
        num = 0
        for i in data:
            if i == k:
                num = num + 1
        return num


class Solution2:
    def GetNumberOfK(self, data, k):
        left = 0
        right = len(data) - 1
        leftk = self.getleftk(data, k, left, right)
        print(leftk)
        rightk = self.getrightk(data, k, left, right)
        print(rightk)
        return rightk - leftk + 1

    def getleftk(self, data, k, left, right):
        while left <= right:
            middle = (left + right) // 2
            if data[middle] < k:
                left = middle + 1
            else:  # 当k等于data[middle]时
                right = middle - 1
        return left

    def getrightk(self, data, k, left, right):
        while left <= right:
            middle = (left + right) // 2
            if data[middle] <= k:  # 当k等于data[middle]时
                left = middle + 1
            else:
                right = middle - 1
        return right


if __name__ == "__main__":
    S = Solution2()
    print(S.GetNumberOfK([1, 2, 2, 5, 6, 7, 12, 14, 15], 2))
