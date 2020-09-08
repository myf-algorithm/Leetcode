#
# Ðý×ª×Ö·û´®
# @param A string×Ö·û´®
# @param B string×Ö·û´®
# @return bool²¼¶ûÐÍ
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
