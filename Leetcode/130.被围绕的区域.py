from typing import List


class UnionFind(object):
    def __init__(self, n: int):
        self._count = n
        self._parent = [i for i in range(n)]
        # 记录每棵树的重量
        self._size = [1] * n

    def union(self, p: int, q: int):
        """ 连接两个节点 """
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        # 将小树接到大树下面：保证树平衡
        if self._size[root_p] > self._size[root_q]:
            self._parent[root_q] = root_p
            self._size[root_p] += self._size[root_q]
        else:
            self._parent[root_p] = root_q
            self._size[root_q] += self._size[root_p]
        self._count -= 1
        return

    def connected(self, p: int, q: int):
        return self.find(p) == self.find(q)

    def find(self, x: int):
        """ 返回某个节点的根节点 """
        while self._parent[x] != x:
            # 压缩路径：使当前节点的父节点指向父节点的父节点
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return x

    def get_count(self):
        return self._count


class Solution(object):
    def solve_DFS(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = "B"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tmp_i = i + x
                tmp_j = j + y
                if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == "O":
                    dfs(tmp_i, tmp_j)

        # 从边界出发，把边界上和'O'连通点变为'B'
        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                dfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                dfs(row - 1, j)

        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                dfs(i, 0)
            # 最后一列
            if board[i][col - 1] == "O":
                dfs(i, col - 1)

        # 再遍历整个board，将'O'变为'X'，将'B'变为'O'
        for i in range(row):
            for j in range(col):
                # O 变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # B 变成 O
                if board[i][j] == "B":
                    board[i][j] = "O"

    def solve_BFS(self, board):
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def bfs(i, j):
            from collections import deque
            queue = deque()
            queue.appendleft((i, j))
            while queue:
                i, j = queue.pop()
                if 0 <= i < row and 0 <= j < col and board[i][j] == "O":
                    board[i][j] = "B"
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        queue.appendleft((i + x, j + y))

        # 从边界出发，把边界上和'O'连通点变为'B'
        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                bfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                bfs(row - 1, j)

        for i in range(row):

            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][col - 1] == "O":
                bfs(i, col - 1)

        # 再遍历整个board，将'O'变为'X'，将'B'变为'O'
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"

    def solve_UnionFindSet(self, board):
        f = {}

        # 返回某个节点的根节点
        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        # 连接两个节点
        def union(x, y):
            f[find(y)] = find(x)

        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        dummy = row * col


        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:    # 将四周的'O'和dummy节点相连
                        union(i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 区域内的'O'和相邻的'O'节点相连
                            if board[i + x][j + y] == "O":
                                union(i * col + j, (i + x) * col + (j + y))
        for i in range(row):
            for j in range(col):
                if find(dummy) == find(i * col + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
