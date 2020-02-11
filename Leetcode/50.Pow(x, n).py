class Solution(object):
    def myPow(self, x, n):
        judge = True
        if n < 0:
            n = -n
            judge = False
        final = 1
        while n > 0:
            if n & 1:  # 代表是奇数
                final *= x
            x *= x
            n >>= 1  # 右移一位
        return final if judge else 1 / final


if __name__ == '__main__':
    S = Solution()
    print(S.myPow(0.00001, 2147483647))
