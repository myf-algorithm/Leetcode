# -*- coding:utf-8 -*-
# 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
# 为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
# 但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,
# 可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # ones记录1出现的个数
        # m记录1的位置处于那一位
        ones, m = 0, 1
        while m <= n:
            # 1.curDig = 0, 商 * 10 ^ (i - 1)
            # 2.curDig = 1, 商 * 10 ^ (i - 1) + 余数 + 1
            # 3.curDig > 1, (商 + 1) * 10 ^ (i - 1)
            ones += (n // m + 8) // 10 * m + (n // m % 10 == 1) * (n % m + 1)
            m *= 10
        return ones


if __name__ == '__main__':
    S = Solution()
    print(S.NumberOf1Between1AndN_Solution(256))
