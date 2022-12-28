class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def backtrack(board):
            for i in range(len(board)):  # 遍历行
                for j in range(len(board[0])):  # 遍历列
                    if board[i][j] != ".":
                        continue
                    for k in range(1, 10):  # (i, j) 这个位置放k是否合适
                        if isValid(i, j, k, board):
                            board[i][j] = str(k)  # 放置k
                            if backtrack(board): return True  # 如果找到合适一组立刻返回
                            board[i][j] = "."  # 回溯，撤销k
                    return False  # 9个数都试完了，都不行，那么就返回false
            return True  # 遍历完没有返回false，说明找到了合适棋盘位置了

        def isValid(row, col, val, board):
            for i in range(9):  # 判断行里是否重复
                if board[row][i] == str(val):
                    return False
            for j in range(9):  # 判断列里是否重复
                if board[j][col] == str(val):
                    return False
            startRow = (row // 3) * 3
            startcol = (col // 3) * 3
            for i in range(startRow, startRow + 3):  # 判断9方格里是否重复
                for j in range(startcol, startcol + 3):
                    if board[i][j] == str(val):
                        return False
            return True

        backtrack(board)