class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0] * col for _ in range(row)]

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            res = 1
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and matrix[tmp_i][tmp_j] > matrix[i][j]:
                    res = max(res, 1 + dfs(tmp_i, tmp_j))
            dp[i][j] = max(res, dp[i][j])
            return dp[i][j]

        return max(dfs(i, j) for i in range(row) for j in range(col))
