#
# 最大乘积
# @param A int整型一维数组
# @return long长整型
#
class Solution:
    def solve(self, A):
        # write code here
        A = sorted(A)
        a, b, c = A[0], A[1], A[-1]
        d, e, f = A[-1], A[-2], A[-3]
        t1 = a * b * c
        t2 = d * e * f
        return t1 if t1 >= t2 else t2
