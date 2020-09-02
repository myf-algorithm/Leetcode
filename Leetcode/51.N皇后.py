from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]  # 初始化二维棋盘
        res = []

        def backtrack(board, row):
            #     if 满足条件:
            #         res.append(路径)
            #         return
            if row == len(board):
                tmp_list = []  # 二维变一维添加到res中
                for e_row in board:
                    tmp = ''.join(e_row)
                    tmp_list.append(tmp)
                res.append(tmp_list)
                return
            #     for 选择 in 选择列表:
            #         做选择
            #         backtrack(路径,选择列表)
            #         撤销选择
            for col in range(len(board[0])):
                if not isValid(board, row, col):
                    # print(isValid(board,row,col))
                    continue
                board[row][col] = 'Q'
                # print(board)
                backtrack(board, row + 1)
                board[row][col] = '.'

        def isValid(board, row, col):
            n = len(board)
            # 检查列是否有皇后互相冲突
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            # 检查右上方是否有皇后互相冲突
            r_row, r_col = row, col
            while r_row > 0 and r_col < n - 1:
                r_row -= 1
                r_col += 1
                if board[r_row][r_col] == 'Q':
                    return False
            # 检查左上方是否有皇后互相冲突
            l_row, l_col = row, col
            while l_row > 0 and l_col > 0:
                l_row -= 1
                l_col -= 1
                if board[l_row][l_col] == 'Q':
                    return False
            return True

        backtrack(board, 0)
        return res


class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 按行枚举
        col, diag, reverse_diag = [0] * n, [0] * 2 * n, [0] * 2 * n
        ret = []
        grid = [['.'] * n for _ in range(n)]

        def dfs(u: int):
            # 终点返回
            if u == n:
                ret.append(["".join(grid[i]) for i in range(n)])
                return
            for i in range(n):
                if not col[i] and not diag[u + i] and not reverse_diag[n - u + i]:
                    grid[u][i] = 'Q'
                    col[i], diag[u + i], reverse_diag[n - u + i] = 1, 1, 1
                    dfs(u + 1)
                    grid[u][i] = '.'
                    col[i], diag[u + i], reverse_diag[n - u + i] = 0, 0, 0

        dfs(0)
        return ret
