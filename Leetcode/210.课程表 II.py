import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        # 存储有向图
        edges = collections.defaultdict(list)
        # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
        visited = [0] * numCourses
        # 用数组来模拟栈，下标 0 为栈底，n-1 为栈顶
        result = list()
        # 判断有向图中是否有环
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            # 将节点标记为「搜索中」
            visited[u] = 1
            # 搜索其相邻节点
            # 只要发现有环，立刻停止搜索
            for v in edges[u]:
                # 如果「未搜索」那么搜索相邻节点
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                # 如果「搜索中」说明找到了环
                elif visited[v] == 1:
                    valid = False
                    return
            # 将节点标记为「已完成」
            visited[u] = 2
            # 将节点入栈
            result.append(u)

        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        if not valid:
            return list()

        # 如果没有环，那么就有拓扑排序
        # 注意下标 0 为栈底，因此需要将数组反序输出
        return result[::-1]

    # BFS
    def findOrder(self, numCourses: int, prerequisites):
        indegrees = [0 for _ in range(numCourses)]  # 入读表
        adjacency = [[] for _ in range(numCourses)]  # 邻接矩阵
        res = []
        queue = []
        for cur, pre in prerequisites:
            indegrees[cur] += 1  # 得到入度
            adjacency[pre].append(cur)  # 得到每个课程节点的邻接表
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)  # 把度为0的课程入队
        while queue:
            pre = queue.pop(0)
            res.append(pre)
            numCourses -= 1  # 每次pre出队时，numCourses减1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1  # 将这个节点的入度减1
                if not indegrees[cur]:  # cur的所有的前驱节点已经被删除，cur入队
                    queue.append(cur)
        return res if not numCourses else []  # 拓扑排序出队次数等于课程个数，课程安排图是否是有向无环图(DAG)，课程可以成功安排
