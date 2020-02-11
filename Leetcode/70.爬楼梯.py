class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        dp
        """
        f = [1, 2]
        for i in range(2, n):
            f.append(f[i - 1] + f[i - 2])
        return f[n - 1]

    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        fib
        """
        a, b = 1, 1
        while n > 0:
            a, b = b, a + b
            n -= 1
        return a

