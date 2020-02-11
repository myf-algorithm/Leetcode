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
        while cnt < size:
            if array[pos] % 2 == 1:
                tmp = array[pos]
                for i in range(pos - 1, -1, -1):
                    array[i + 1] = array[i]
                array[0] = tmp
            else:
                pos -= 1
            cnt += 1
        return array




if __name__ == '__main__':
    S = Solution()
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print(S.reOrderArray(a))
