# -*- coding:utf-8 -*-
# 统计一个数字在排序数组中出现的次数。


class Solution:
    def GetNumberOfK1(self, data, k):
        num = 0
        for i in data:
            if i == k:
                num = num + 1
        return num

    def GetNumberOfK(self, data, k):
        if len(data) < 1:
            return 0
        mid = len(data) // 2
        if data[mid] == k:
            start, end = mid, mid
            for i in range(mid, -1, -1):
                if data[i] == k: start -= 1
            for j in range(mid + 1, len(data)):
                if data[j] == k: end += 1
            return end - start
        elif data[mid] > k:
            return self.GetNumberOfK(data[:mid], k)
        else:
            return self.GetNumberOfK(data[mid + 1:], k)


if __name__ == "__main__":
    S = Solution()
    print(S.GetNumberOfK([1, 2, 2, 5, 6, 7, 12, 14, 15], 2))
