class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        h = {}
        for a in A:
            for b in B:
                if - a - b in h:
                    h[- a - b] += 1
                else:
                    h[- a - b] = 1
        return sum(h[c + d] for c in C for d in D if c + d in h)
