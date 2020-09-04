class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])  # 矩阵的行数，列数
        seen = [[False] * C for _ in matrix]  # 初始化集合，记录已经走过的坐标
        ans = []  # 初始化，存储遍历后的矩阵元素
        dr = [0, 1, 0, -1]  # 方向是：右，下，左，上
        dc = [1, 0, -1, 0]
        r = c = di = 0  # 矩阵元素，方向变量初始化
        for _ in range(R * C):
            ans.append(matrix[r][c])  # 存储遍历矩阵过的元素
            seen[r][c] = True  # 存储遍历过的坐标
            cr, cc = r + dr[di], c + dc[di]  # 先记录下一步坐标，用于判断下一步怎么走
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:  # 判断坐标是否需变向，且没有遍历过
                r, c = cr, cc
            else:
                di = (di + 1) % 4  # 改变方向，右下左上为一圈，防止方向坐标越界
                r, c = r + dr[di], c + dc[di]  # 下一步坐标
        return ans


if __name__ == '__main__':
    S = Solution()
    print(S.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
