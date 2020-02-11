class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 0
        while n >= 5:
            n = n // 5
            p += n
        return p