class Solution(object):
    def countPrimes_naive(self, n: int) -> int:
        def is_prime(num):
            j = 2
            while j * j <= num:
                if num % j == 0:
                    return False
                j += 1
            return True

        count = 0
        for i in range(2, n):
            if is_prime(i):
                count += 1

        return count

    def countPrimes(self, n: int) -> int:
        is_prime = [1] * n

        count = 0
        for i in range(2, n):
            # 将质数的倍数都标记为合数
            if is_prime[i]:
                count += 1
                for j in range(i * i, n, i):
                    is_prime[j] = 0
        return count
