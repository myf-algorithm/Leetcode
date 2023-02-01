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
    def dfs(self, m, i, j, word_idx):
        if i < 0 or i >= len(m) or j < 0 or j >= len(m[0]) or self.visted[i][j] or m[i][j] != self.word[word_idx]:
            # 边界值越界 / 已走过 / 值不同
            return False
        if word_idx == len(self.word) - 1:
            return True
        self.visted[i][j] = 1
        # 左下右上的顺序遍历
        res = self.dfs(m, i, j - 1, word_idx + 1) or \
              self.dfs(m, i + 1, j, word_idx + 1) or \
              self.dfs(m, i, j + 1, word_idx + 1) or \
              self.dfs(m, i - 1, j, word_idx + 1)
        self.visted[i][j] = 0
        return res

    def hasPath(self, matrix, word):
        self.word = word
        self.visted = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        word_idx = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if self.dfs(matrix, row, col, word_idx):
                    return True
        return False


if __name__ == '__main__':
    S = Solution()
    print(S.hasPath(['a', 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e'], 3, 4, 'bcced'))
