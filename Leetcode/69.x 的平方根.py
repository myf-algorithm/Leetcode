class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r * r > x:
            r = (r + x / r) // 2
        return int(r)

    def mySqrt_div(self, x):
        left = 0
        right = x // 2 + 1
        while left < right:
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) >> 1
            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                left = mid
        return left