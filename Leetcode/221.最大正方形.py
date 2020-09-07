from typing import List


# dp[i][j]是代表的以坐标点(i,j)为右下角的最大正方形的边长，这个正方形右下角是(i,j)点才可以
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 and len(matrix[0]) == 0:
            return 0
        maxSide = 0

        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                maxSide = max(maxSide, dp[i][j])
        maxSquare = maxSide * maxSide
        return maxSquare
