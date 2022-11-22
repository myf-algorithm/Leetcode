import bisect
import random
from itertools import accumulate

class Solution:
    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))
        self.total = sum(w)

    def pickIndex(self) -> int:
        x = random.random.randint(1, self.total)
        return bisect.bisect_left(self.pre, x)
