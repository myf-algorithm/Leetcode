import math

class Solution:
    def cross_entropy(self , p , q ):
        res = 0
        for i in range(len(p)):
            res -= p[i] * math.log(q[i],10)
        return '{:.5f}'.format(res)


S = Solution()
print(S.cross_entropy([0, 0.5, 0.5], [0.2, 0.2, 0.6]))
