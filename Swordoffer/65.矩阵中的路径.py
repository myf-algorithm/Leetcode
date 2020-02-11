# -*- coding:utf-8 -*-
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一个格子开始，
# 每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
# 如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
# 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
# 但是矩阵中不包含"abcb"路径，
# 因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
# 路径不能再次进入该格子。

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if len(matrix) == 0 or len(matrix) != rows * cols or len(path) == 0:
            return False
        visited = [False] * len(matrix)
        pathlength = [0]
        # 以矩阵中每一个位置作为起点进行搜索
        for i in range(rows):
            for j in range(cols):
                if self.haspath(matrix, rows, cols, path, j, i, visited, pathlength):
                    return True
        return False

    # 判断矩阵位置（x,y）的字符能否加入已找到的路径中
    def haspath(self, matrix, rows, cols, path, x, y, visited, pathlength):
        '''
        :param matrix:字符矩阵
        :param rows:矩阵的行数
        :param cols:矩阵的列数
        :param path:需要寻找的路径
        :param x:当前位置的横坐标(对应列数)
        :param y:当前位置的纵坐标(对应行数)
        :param visited:访问标志数组
        :param pathlength:已经找到的路径长度
        :return:是否存在路径
        '''
        if pathlength[0] == len(path):
            return True
        curhaspath = False
        # 参数校验：
        # 1、位置坐标不超过行列数
        # 2、当前位置字符等于路径中对应位置的字符
        # 3、当前位置未存在于当前已找到的路径中
        if 0 <= x < cols \
                and 0 <= y < rows \
                and matrix[y * cols + x] == path[pathlength[0]] \
                and not visited[y * cols + x]:
            visited[y * cols + x] = True
            pathlength[0] += 1
            # 分别向左，向右，向上，向下移动一个格子，任一方向能够继续往下走均可
            curhaspath = self.haspath(matrix, rows, cols, path, x - 1, y, visited, pathlength) \
                         or self.haspath(matrix, rows, cols, path, x, y - 1, visited, pathlength) \
                         or self.haspath(matrix, rows, cols, path, x + 1, y, visited, pathlength) \
                         or self.haspath(matrix, rows, cols, path, x, y + 1, visited, pathlength)
            # 如果不能再走下一步，需要回退到上一状态
            if not curhaspath:
                pathlength[0] -= 1
                visited[y * cols + x] = False
        return curhaspath


if __name__ == '__main__':
    S = Solution()
    print(S.hasPath(['a', 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e'], 3, 4, 'bcced'))
