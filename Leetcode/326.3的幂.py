class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and (1162261467 % n == 0)

    def isPowerOfThree1(self, n):
        if n > 1:
            while n % 3 == 0:
                n //= 3
        return n == 1
