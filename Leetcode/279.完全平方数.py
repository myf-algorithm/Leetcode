class node:
    def __init__(self, value, step=0):
        self.value = value
        self.step = step

    def __str__(self):
        return '<value:{}, step:{}>'.format(self.value, self.step)


class Solution(object):
    def numSquares_dp(self, n):
        """
        :type n: int
        :rtype: int
        dp[i]代表到数字i组成最少完全平方个数
        动态转移方程：dp[i] = min(dp[i], dp[i - j * j] + 1), j <= sqrt{i} + 1
        """
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]

    def numSquares_bfs(self, n):
        """
        :type n: int
        :rtype: int
        BFS 其实是很简单的基础算法，抓住如下几点即可轻松写出不易错的 baseline:

        BFS 算法组成的 3 元素：队列，入队出队的节点，已访问的集合。
            队列：先入先出的容器；
            节点：最好写成单独的类，比如本例写成 (value,step) 元组。也可写成 (value,visited)，看自己喜好和题目；
            已访问集合：为了避免队列中插入重复的值

        BFS算法组成的套路：
            初始化三元素：
            Node = node(n) queue = [Node] visited = set([Node.value])
            操作队列 —— 弹出队首节点：
            vertex = queue.pop(0)
            操作弹出的节点 —— 根据业务生成子节点（一个或多个）：
            [node(vertex.value - n*n, Node.step+1) for n in range(1,int(vertex.value**.5)+1)]
            判断这些节点 —— 符合业务条件，则return，不符合业务条件，且不在已访问集合，则追加到队尾，并加入已访问集合：

            if i==0:
                return new_vertex.step

            elif i not in visited:
                queue.append(new_vertex)
                visited.add(i)

            若以上遍历完成仍未return，下面操作返回未找到代码：
            return -1
        """
        queue = [node(n)]
        visited = set([node(n).value])
        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value - n * n for n in range(1, int(vertex.value ** .5) + 1)]
            for i in residuals:
                new_vertex = node(i, vertex.step + 1)
                if i == 0:
                    return new_vertex.step
                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)
        return -1
