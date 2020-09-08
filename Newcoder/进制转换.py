#
# ����ת��
# @param M int���� ��������
# @param N int���� ת�����Ľ���
# @return string�ַ���
#
class Solution:
    def solve(self, M, N):
        out = []
        mp = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        flg = 1
        if M < 0:
            flg = -1
            M = M * flg
        while M >= 1:
            if M % N >= 10:
                out.append(mp[M % N])
            else:
                out.append(str(M % N))
            M = M / N
        out.reverse()
        if flg == 1:
            return ''.join([str(x) for x in out])
        else:
            return '-' + ''.join([str(x) for x in out])
