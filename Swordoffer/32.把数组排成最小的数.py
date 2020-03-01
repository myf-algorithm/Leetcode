# -*- coding:utf-8 -*-
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
# 打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
# 则打印出这三个数字能排成的最小数字为321323。

# 比较两个字符串s1, s2大小的时候，先将它们拼接起来，比较s1+s2,和s2+s1那个大
# 如果s1+s2大，那说明s2应该放前面，所以按这个规则，s2就应该排在s1前面


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
    print(S.PrintMinNumber([3, 32, 321]))
