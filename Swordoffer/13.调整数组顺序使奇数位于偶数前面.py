# -*- coding:utf-8 -*-
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。


class Solution:
    def reOrderArray(self, array):
        even, odd = [], []
        for i in array:
            if i % 2 == 0:
                odd.append(i)
            else:
                even.append(i)
        return even + odd


class Solution1:
    def reOrderArray(self, array):
        size = len(array)
        pos = size - 1
        cnt = 0
        # pos从后往前开始遍历
        while cnt < size:
            if array[pos] % 2 == 1:  # 当前数值为奇数
                tmp = array[pos]  # 暂存当前值到tmp
                for i in range(pos - 1, -1, -1):  # 当前位置到倒数第二个位置整体向后移动一个位置
                    array[i + 1] = array[i]
                array[0] = tmp  # 移动完毕后，array[0]赋值为tmp
            else:
                pos -= 1
            cnt += 1
        return array


from collections import deque


class Solution2:
    def reOrderArray(self, array):
        d = deque()
        for i in range(len(array)):
            if array[i] % 2 == 0:
                a.append(array[i])
            if array[len(array) - i - 1] % 2 == 1:
                d.appendleft(array[len(array) - i - 1])
        return list(d)


if __name__ == '__main__':
    S = Solution()
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print(S.reOrderArray(a))
