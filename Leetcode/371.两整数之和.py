class Solution(object):
    def getSum(self, a, b):
        # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            carry = (a & b) << 1  # 计算进位结果
            a = (a ^ b) % MASK  # 无进位加法，取余范围限制在 [0, 2^32-1] 范围内
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
