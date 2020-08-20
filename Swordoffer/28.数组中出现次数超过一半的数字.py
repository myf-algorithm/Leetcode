# -*- coding:utf-8 -*-
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。


class Solution:
    # 使用字典进行计数
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


# 想象下面示例的情况：
# 1 1 1 1 1 1
# 2 3 4 5
class Solution1:
    # 使用不同数字进行对消的方法
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


class Solution2:
    # 使用默认词典的方法
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        d = {}
        d[1] = 2
        for num in numbers:
            d[num] = d.setdefault(num, 0) + 1
        for key in d.keys():
            if d[key] * 2 > length:
                return int(key)
        return 0

    def MoreThanHalfNum_Solution1(self, numbers):
        from collections import Counter
        count_dic = Counter(numbers)
        length = len(numbers)
        for k, v in count_dic.items():
            if v * 2 > length:
                return k
        return 0


if __name__ == '__main__':
    S = Solution1()
    print(S.MoreThanHalfNum_Solution([1, 2, 2]))
