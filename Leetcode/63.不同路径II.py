class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m < 1:
            return 0
        n = len(obstacleGrid[0])
        if n < 1:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif 0 == i and 0 != j:
                    if 0 == obstacleGrid[i][j]:
                        dp[i][j] = dp[i][j - 1]
                elif 0 != i and 0 == j:
                    if 0 == obstacleGrid[i][j]:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if 0 == obstacleGrid[i][j]:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
