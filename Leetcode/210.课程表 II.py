class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
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
