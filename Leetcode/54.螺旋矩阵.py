class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])  # ���������������
        seen = [[False] * C for _ in matrix]  # ��ʼ�����ϣ���¼�Ѿ��߹�������
        ans = []  # ��ʼ�����洢������ľ���Ԫ��
        dr = [0, 1, 0, -1]  # �����ǣ��ң��£�����
        dc = [1, 0, -1, 0]
        r = c = di = 0  # ����Ԫ�أ����������ʼ��
        for _ in range(R * C):
            ans.append(matrix[r][c])  # �洢�����������Ԫ��
            seen[r][c] = True  # �洢������������
            cr, cc = r + dr[di], c + dc[di]  # �ȼ�¼��һ�����꣬�����ж���һ����ô��
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:  # �ж������Ƿ��������û�б�����
                r, c = cr, cc
            else:
                di = (di + 1) % 4  # �ı䷽����������ΪһȦ����ֹ��������Խ��
                r, c = r + dr[di], c + dc[di]  # ��һ������
        return ans


if __name__ == '__main__':
    S = Solution()
    print(S.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
