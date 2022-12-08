# 环检测算法，DFS、BFS
from collections import deque


class Solution:
    # DFS
    def canFinish_DFS(self, numCourses: int, prerequisites) -> bool:
        # 先根据依赖关系建图
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            pre = edge[1]
            cur = edge[0]
            # 建立课程从pre到to的依赖
            graph[pre].append(cur)

        # 记录当前 traverse 经过的路径
        onpath = [False for _ in range(numCourses)]
        # 标记节点被遍历的情况
        visited = [False for _ in range(numCourses)]
        self.hascycle = False

        # DFS遍历函数
        def traverse(graph, v):
            # 如果当前traverse经过的路径已经遍历过了 说明有环
            if onpath[v]:
                self.hascycle = True
            if visited[v] or self.hascycle:
                # 如果节点已经被遍历或找到了环 就不继续遍历了
                return
            # 标记节点v为已访问
            visited[v] = True
            # 前序位置 标记进入节点v的遍历
            onpath[v] = True
            for neighbor in graph[v]:
                traverse(graph, neighbor)
            # 后序位置 离开节点v的遍历
            onpath[v] = False

        # 由于图可能不是全联通的 所以需要对每个节点都调用一次遍历函数
        for i in range(numCourses):
            # 遍历每个节点
            traverse(graph, i)

        # 只要没有循环依赖（环）就说明可以完成所有课程，否则不能
        return not self.hascycle

    # BFS
    def canFinish_BFS(self, numCourses: int, prerequisites) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]

        queue = deque()
        for cur, pre in prerequisites:
            # 统计每个节点的入度
            indegrees[cur] += 1
            # 得到图的邻接表
            adjacency[pre].append(cur)

        for i in range(len(indegrees)):
            # 将所有入度为 0 的节点入队
            if not indegrees[i]:
                queue.append(i)

        # 当 queue 非空时，依次将队首节点出队，在课程安排图中删除此节点 pre
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                # cur 所有的前驱节点已经被删除
                if not indegrees[cur]:
                    queue.append(cur)
        # 若课程安排图中存在环，一定有节点的入度始终不为 0
        return not numCourses