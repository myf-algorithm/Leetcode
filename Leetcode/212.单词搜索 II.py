class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for word in words:
            t = trie
            for w in word:
                t = t.setdefault(w, {})
            t["end"] = 1
        res = []
        row = len(board)
        col = len(board[0])

        def dfs(i, j, trie, s):
            c = board[i][j]
            if c not in trie:
                return
            trie = trie[c]
            if "end" in trie and trie["end"] == 1:
                res.append(s + c)
                trie["end"] = 0  # 防止重复数组加入
            board[i][j] = "#"
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and board[tmp_i][tmp_j] != "#":
                    dfs(tmp_i, tmp_j, trie, s + c)
            board[i][j] = c

        for i in range(row):
            for j in range(col):
                dfs(i, j, trie, "")
        return res

    def findWords_bfs(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        d = {}
        for s in words:
            t = d
            for c in s:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['word'] = s
        ans = []

        def bfs(i, j):
            que = [([(i, j)], d[board[i][j]])]
            tmp_ans = []
            while que:
                tmp = []
                for vst, t in que:
                    if 'word' in t:
                        ans.append(t.pop('word'))
                    xi, yi = vst[-1]
                    for x, y in [(xi + 1, yi), (xi - 1, yi), (xi, yi + 1), (xi, yi - 1)]:
                        if 0 <= x < m and 0 <= y < n and (x, y) not in vst and board[x][y] in t:
                            tmp += [(vst + [(x, y)], t[board[x][y]])]
                que = tmp

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in d:
                    bfs(i, j)
        return sorted(ans)
