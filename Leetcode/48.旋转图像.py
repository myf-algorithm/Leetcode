class Solution(object):
    def rotate(self, matrix):
        # 进行矩阵的转置
        for x in range(len(matrix)):
            for y in range(x):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

        # 转置后进行列变换
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) // 2):
                matrix[i][j], matrix[i][len(matrix) - 1 - j] = matrix[i][len(matrix) - 1 - j], matrix[i][j]


if __name__ == '__main__':
    S = Solution()
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    S.rotate(matrix)
    print(matrix)
