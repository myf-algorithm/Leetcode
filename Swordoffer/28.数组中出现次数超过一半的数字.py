# -*- coding:utf-8 -*-
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        dict = {}
        for i in numbers:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i] + 1
            if dict[i] > len(numbers) / 2:
                return i
        return 0


class Solution1:
    def MoreThanHalfNum_Solution(self, numbers):
        if numbers == []:
            return 0
        val, cnt = None, 0
        for num in numbers:
            if cnt == 0:
                val, cnt = num, 1
            elif val == num:
                cnt += 1
            else:
                cnt -= 1
        return val if numbers.count(val) * 2 > len(numbers) else 0


if __name__ == '__main__':
    S = Solution1()
    print(S.MoreThanHalfNum_Solution([1, 2, 2]))
