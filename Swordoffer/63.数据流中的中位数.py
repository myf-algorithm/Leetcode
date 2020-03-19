# -*- coding:utf-8 -*-
# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
# 那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
# 那么中位数就是所有数值排序之后中间两个数的平均值。
# 我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
from heapq import *


class Solution:
    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0

    def Insert(self, num):
        if self.count & 1 == 0:  # count为偶数
            self.left.append(num)
        else:  # count为奇数
            self.right.append(num)
        self.count += 1

    def GetMedian(self, x):
        if self.count == 1:
            return self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.left[0] > self.right[0]:
            self.left[0], self.right[0] = self.right[0], self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.count & 1 == 0:
            return (self.left[0] + self.right[0]) / 2.0
        else:
            return self.left[0]

    def MaxHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length // 2 - 1, -1, -1):
            k = i
            temp = alist[k]
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index] < alist[index + 1]: index += 1
                if temp >= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp

    def MinHeap(self, alist):
        length = len(alist)
        if alist == None or length <= 0:
            return
        if length == 1:
            return alist
        for i in range(length // 2 - 1, -1, -1):
            k = i
            temp = alist[k]
            heap = False
            while not heap and 2 * k < length - 1:
                index = 2 * k + 1
                if index < length - 1:
                    if alist[index] > alist[index + 1]: index += 1
                if temp <= alist[index]:
                    heap = True
                else:
                    alist[k] = alist[index]
                    k = index
            alist[k] = temp


class Solution1:
    def __init__(self):
        self.heaps = [], []

    def Insert(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def GetMedian(self, x):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


import heapq


class Solution2:
    def __init__(self):
        self.count = 0  # 定义计数变量
        self.max_heap = []  # 定义最大堆
        self.min_heap = []  # 定义最小堆

    def Insert(self, num):
        self.count += 1 # 计数累加
        # 将数据放到最大堆中
        heapq.heappush(self.max_heap, -num)
        # 将最大堆中的堆顶元素放到最小堆中
        max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -max_heap_top)
        # 如果最小堆和最大堆之间的差距大于1，将最小堆中的堆顶放进最大堆
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_top)

    def GetMedian(self, s):
        if self.count & 1:
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2.0


if __name__ == '__main__':
    S = Solution1()
    S.Insert(1)
    S.Insert(2)
    S.Insert(3)
    S.Insert(4)
    S.Insert(5)
    print(S.GetMedian(1))
