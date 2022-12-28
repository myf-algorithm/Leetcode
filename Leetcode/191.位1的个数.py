import collections
from typing import List


def hammingWeight1(self, n: int) -> int:
    count = 0
    for i in range(32):
        if (n >> i) & 1:
            count += 1
    return count


def hammingWeight2(self, n: int) -> int:
    return collections.Counter(str(bin(n)))['1']


def hammingWeight3(self, n: int) -> int:
    res = 0
    while n != 0:
        n = n & (n - 1)  # 可以消掉最后一位1
        res += 1
    return res
