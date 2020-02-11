# -*- coding:utf-8 -*-
# 求1 + 2 + 3 + ... + n，要求不能使用乘除法、for、while、if、else、switch、case等
# 关键字及条件判断语句（A ? B : C）

# 思路：
# 不计进位的和为 a ^ b，进位就是 a & b
# a + b = a ^ b + (a & b) << 1


class Solution:
    def Add_sum(self, num1, num2):
        num = [num1, num2]
        return sum(num)

    def Add(self, num1, num2):
        unit = num1 ^ num2
        carry_bit = num1 & num2
        while carry_bit != 0:
            temp_a = unit
            temp_b = carry_bit << 1
            unit = temp_a ^ temp_b
            carry_bit = temp_a & temp_b
        return unit


if __name__ == '__main__':
    S = Solution()
    print(S.Add(100, 12))