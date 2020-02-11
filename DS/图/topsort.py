# 有向无环图（Directed Acyclic Graph, DAG），图中不存在回路，一定存在拓扑排序
# 拓扑排序，拓扑排序并不唯一

# 顶点表示活动，弧表示活动间的优先关系的有向图，称为顶点表示活动的网（Activity On Vertex Nertwork，AOV）

# 弧表示活动，AOE网，分别有一个源点和一个汇点
# 顶点表示事件，弧表示活动，权表示活动持续的时间
# 各个活动所持续的时间之和为路径长度，源点到汇点最大长度的路径为关键路径，关键路径上的活动为关键活动
# 完成整个工程的最短时间就是关键路径的长度，关键路径上边的权值总和


def toposort(graph):
    in_degrees = dict((u, 0) for u in graph)  # 初始化所有顶点入度为0
    vertex_num = len(in_degrees)
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1  # 计算每个顶点的入度
    Q = [u for u in in_degrees if in_degrees[u] == 0]  # 筛选入度为0的顶点
    Seq = []
    while Q:
        u = Q.pop()  # 默认从最后一个删除
        Seq.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1  # 移除其所有指向
            if in_degrees[v] == 0:
                Q.append(v)  # 再次筛选入度为0的顶点
    if len(Seq) == vertex_num:  # 如果循环结束后存在非0入度的顶点说明图中有环，不存在拓扑排序
        return Seq
    else:
        print("there's a circle.")


if __name__ == '__main__':
    G = {
        'a': 'bce',
        'b': 'd',
        'c': 'd',
        'd': '',
        'e': 'cd'
    }
    print(toposort(G))
