# ��ȱʧ����
# @param a int����һά���� ���������ִ�
# @return int����

class Solution:
    def solve(self, a):
        # write code here
        if len(a) == 0:
            return 0
        if a[0] == 1:
            return 0
        for i in range(1, len(a)):
            if a[i - 1] + 1 != a[i]:
                return a[i - 1] + 1
