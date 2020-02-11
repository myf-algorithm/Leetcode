class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrimes = [1] * n
        res = 0
        for i in range(2, n):
            if isPrimes[i] == 1:
                res += 1
            j = i
            while i * j < n:
                isPrimes[i * j] = 0
                j += 1
        return res

    def countPrimes_1(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        isPrimes = [1] * n
        isPrimes[0] = isPrimes[1] = 0
        # 在 2 到 根号n 的范围内，当一个数是质数，将它所有的比n小的倍数设置成0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrimes[i] == 1:
                isPrimes[i * i: n: i] = [0] * len(isPrimes[i * i: n: i])
        return sum(isPrimes)

