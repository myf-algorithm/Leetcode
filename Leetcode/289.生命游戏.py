class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        # 记录每一个位置周围的活细胞的个数
        recording = [[0] * col for _ in range(row)]

        def helper(i, j):
            ans = 0
            for x, y in [[-1, -1],
                         [-1, 0],
                         [-1, 1],
                         [0, -1],
                         [0, 1],
                         [1, -1],
                         [1, 0],
                         [1, 1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and board[tmp_i][tmp_j] == 1:
                    ans += 1
            return ans

        for i in range(row):
            for j in range(col):
                recording[i][j] = helper(i, j)
        for i in range(row):
            for j in range(col):
                # 根据条件判断
                if board[i][j] == 0 and recording[i][j] == 3:
                    board[i][j] = 1
                if board[i][j] == 1 and (recording[i][j] < 2 or recording[i][j] > 3):
                    board[i][j] = 0

    def gameOfLife_bit(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        for i in range(0, rows):
            for j in range(0, cols):
                lives = self.liveNeighbours(board, rows, cols, i, j)
                if board[i][j] == 1 and 2 <= lives <= 3:
                    board[i][j] = 3

                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        for i in range(0, rows):
            for j in range(0, cols):
                board[i][j] >>= 1

    def liveNeighbours(self, board, rows, cols, i, j):
        direction = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        count = 0
        for d in direction:
            ni, nj = d[0] + i, d[1] + j
            if 0 <= ni < rows and 0 <= nj < cols:
                count += (board[ni][nj] & 1)
        return count
