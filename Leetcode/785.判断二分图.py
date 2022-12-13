# dfs
class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n
        valid = True

        def dfs(node, c):
            nonlocal valid
            color[node] = c
            cNei = (GREEN if c == RED else RED)
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:  # 未染色
                    dfs(neighbor, cNei)
                    if not valid:
                        return
                elif color[neighbor] != cNei:  # 已染色，但不对
                    valid = False
                    return

        for i in range(n):
            if color[i] == UNCOLORED:
                dfs(i, RED)
                if not valid:
                    break

        return valid


import collections


# bfs
class Solution1:
    def isBipartite(self, graph):
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n

        for i in range(n):
            if color[i] == UNCOLORED:
                q = collections.deque([i])
                color[i] = RED
                while q:
                    node = q.popleft()
                    cNei = (GREEN if color[node] == RED else RED)
                    for neighbor in graph[node]:
                        if color[neighbor] == UNCOLORED:  # 未染色
                            q.append(neighbor)
                            color[neighbor] = cNei
                        elif color[neighbor] != cNei:  # 已染色，但不对
                            return False
        return True
