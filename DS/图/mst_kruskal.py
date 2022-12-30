# Kruskal算法
# Kruskal算法描述:
# 1).记Graph中有v个顶点，e个边
# 2).新建图Graphnew，Graphnew中拥有原图中相同的e个顶点，但没有边
# 3).将原图Graph中所有e个边按权值从小到大排序
# 4).循环：从权值最小的边开始遍历每条边，直至图Graph中所有的节点都在同一个连通分量中
#       if 这条边连接的两个节点于图Graphnew中不在同一个连通分量中
#           添加这条边到图Graphnew中

# Prim算法每次只加入一个点，适用于边比较密集的图
# Kruskal算法根据权重对所有的边排序，适用于边比较稀疏的图


def kruskal(graph):
    assert type(graph) == dict
    nodes = graph.keys()
    visited = set()
    path = []
    next = None
    while len(visited) < len(nodes):
        distance = float('inf')
        for s in nodes:
            for d in nodes:
                if s in visited and d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    pre = s
                    next = d
        path.append((pre, next))
        visited.add(pre)
        visited.add(next)
    return path


if __name__ == '__main__':
    graph_dict = {"s1": {"s1": 0, "s2": 6, "s10": 3, "s12": 4, "s5": 3},
                  "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 3, "s5": 4},
                  "s10": {"s1": 2, "s2": 6, "s10": 0, "s12": 3, "s5": 4},
                  "s12": {"s1": 1, "s2": 5, "s10": 2, "s12": 0, "s5": 2},
                  "s5": {"s1": 3, "s2": 5, "s10": 7, "s12": 4, "s5": 0},
                  }
    path = kruskal(graph_dict)
    print(path)
