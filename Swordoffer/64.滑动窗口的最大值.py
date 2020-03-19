# -*- coding:utf-8 -*-
# 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
# 例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
# 那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
# 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
# {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}，
# {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}，
# {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。


class Solution:
    def maxInWindows(self, num, size):
        if size <= 0 or len(num) <= 0:
            return []
        res = []
        for i in range(len(num) - size + 1):
            res.append(max(num[i:i + size]))
        return res

    def maxInWindows_deque(self, num, size):
        if num == None or size <= 0:
            return []
        deque = []
        if len(num) >= size:
            index = []  # 存储索引的列表
            # 首先遍历前size个元素
            for i in range(size):
                while len(index) > 0 and num[i] > num[index[-1]]:  # 如果当前元素比前一个元素大
                    index.pop()  # 将前一个元素索引删掉
                index.append(i)  # 将当前元素索引加入
            for i in range(size, len(num)):
                deque.append(num[index[0]])  # 加入当前窗口的最大值
                while len(index) > 0 and num[i] > num[index[-1]]:  # 如果当前元素比前一个元素大
                    index.pop()  # 将前一个元素索引删掉
                if len(index) > 0 and index[0] <= i - size:  # 如果索引列表长度大于size
                    index.pop(0)  # 弹出索引列表的头元素
                index.append(i)  # 将当前元素索引加入
            deque.append(num[index[0]])  # 加入当前窗口的最大值
        return deque


if __name__ == '__main__':
    S = Solution()
    print(S.maxInWindows_deque([1, 2, 3, 4, 5, 6], 2))
