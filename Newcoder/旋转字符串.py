#
# ��ת�ַ���
# @param A string�ַ���
# @param B string�ַ���
# @return bool������
#
class Solution:
    def solve(self, A, B):
        # write code here
        if not A and not B:
            return True

        res = []
        n = len(A)
        for i in range(n):
            res.append(A[i:] + A[:i])
        if B in res:
            return True
        else:
            return False
