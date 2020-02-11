# -*- coding:utf-8 -*-
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。
# 数组中某些数字是重复的，但不知道有几个数字是重复的。
# 也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
# 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，
# 那么对应的输出是第一个重复的数字2。


class Solution:
    def duplicate(self, numbers, duplication):
        dic = {}
        if not numbers:
            return False
        for i in numbers:
            if i not in dic:
                dic[i] = 1
            else:
                if dic[i] == 1:
                    duplication[0] = i
                    return True
        return False


"""
举例说明：{2,3,1,0,2,5,3}：

0(索引值)和2(索引值位置的元素)不相等，
并且2(索引值位置的元素)和1(以该索引值位置的元素2为索引值的位置的元素)不相等，
则交换位置，数组变为：{1,3,2,0,2,5,3}；

0(索引值)和1(索引值位置的元素)仍然不相等，
并且1(索引值位置的元素)和3(以该索引值位置的元素1为索引值的位置的元素)不相等，
则交换位置，数组变为：{3,1,2,0,2,5,3}；

0(索引值)和3(索引值位置的元素)仍然不相等，
并且3(索引值位置的元素)和0(以该索引值位置的元素3为索引值的位置的元素)不相等，
则交换位置，数组变为：{0,1,2,3,2,5,3}；

0(索引值)和0(索引值位置的元素)相等，遍历下一个元素；
1(索引值)和1(索引值位置的元素)相等，遍历下一个元素；
2(索引值)和2(索引值位置的元素)相等，遍历下一个元素；
3(索引值)和3(索引值位置的元素)相等，遍历下一个元素；

4(索引值)和2(索引值位置的元素)不相等，
但是2(索引值位置的元素)和2(以该索引值位置的元素2为索引值的位置的元素)相等，
则找到了第一个重复的元素。
"""


class Solution1:
    def duplicate(self, numbers, duplication):
        n = len(numbers)
        if n == 0:
            return False
        for i in range(n):
            if numbers[i] < 0 or numbers[i] > n - 1:
                return False
        for i in range(n):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
        return False


class Solution2:
    def duplicate(self, numbers, duplication):
        n = len(numbers)
        if n == 0:
            return False
        for i in range(n):
            index = numbers[i]
            if index >= n:
                index -= n
            if numbers[index] >= n:
                duplication[0] = index
                return True
            numbers[index] += n
        return False


if __name__ == '__main__':
    S = Solution1()
    res = [1]
    print(S.duplicate([2, 1, 3, 1, 4], res))
    print(res)
