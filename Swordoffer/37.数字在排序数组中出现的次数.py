# -*- coding:utf-8 -*-
# 统计一个数字在排序数组中出现的次数。


class Solution:
    def GetNumberOfK(self, data, k):
        num = 0
        for i in data:
            if i == k:
                num = num + 1
        return num


class Solution1:
    def GetNumberOfK(self, data, k):
        """
        二分查找到给定的数字及其坐标
        以该坐标为中点，向前向后找到这个数字的始–终位置
        """
        if len(data) < 1:
            return 0
        mid = len(data) // 2
        if data[mid] == k:
            start, end = mid, mid
            for i in range(mid, -1, -1):
                if data[i] == k:
                    start -= 1
            for j in range(mid + 1, len(data)):
                if data[j] == k:
                    end += 1
            return end - start
        elif data[mid] > k:
            return self.GetNumberOfK(data[:mid], k)
        else:
            return self.GetNumberOfK(data[mid + 1:], k)


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
            if data[middle] < k:  # k必须严格大于data[middle]
                left = middle + 1
            else:
                right = middle - 1
        return left

    def getrightk(self, data, k, left, right):
        while left <= right:
            middle = (left + right) // 2
            if data[middle] <= k:
                left = middle + 1
            else:
                right = middle - 1
        return right


if __name__ == "__main__":
    S = Solution2()
    print(S.GetNumberOfK([1, 2, 2, 5, 6, 7, 12, 14, 15], 2))
