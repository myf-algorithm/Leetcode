# -*- coding:utf-8 -*-
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
# 打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
# 则打印出这三个数字能排成的最小数字为321323。


class Solution:
    def PrintMinNumber(self, numbers):
        from functools import cmp_to_key
        if not numbers:
            return ""
        numbers = list(map(str, numbers))
        numbers.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)))
        return '0' if numbers[0] == '0' else ''.join(numbers)


if __name__ == '__main__':
    S = Solution()
    print(S.PrintMinNumber([1, 2, 3, 4, 5, 6, 7, 0]))
