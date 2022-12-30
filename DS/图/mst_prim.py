# 连通图：G=(V,E)
# 生成树：G'=(V,E')
# 带权连通图，生成树的权
# 权最小的生成树叫做最小生成树（MST）

# Prim算法描述：
# 1).输入：一个加权连通图，其中顶点集合为V，边集合为E；
# 2).初始化：Vnew = {x}，其中x为集合V中的任一节点（起始点），Enew = {},为空；
# 3).重复下列操作，直到Vnew = V：
#   a.在集合E中选取权值最小的边<u, v>，其中u为集合Vnew中的元素，而v不在Vnew集合当中，并且v∈V，
#       如果存在有多条满足前述条件即具有相同权值的边，则可任意选取其中之一；
#   b.将v加入集合Vnew中，将<u, v>边加入集合Enew中；
# 4).输出：使用集合Vnew和Enew来描述所得到的最小生成树。


def prim(graph, vertex_num):
    INF = 1 << 10
    visit = [False] * vertex_num
    dist = [INF] * vertex_num
    preindex = [0] * vertex_num
    for i in range(vertex_num):
        minDist = INF + 1
        nextIndex = -1
        for j in range(vertex_num):
            if dist[j] < minDist and not visit[j]:
                minDist = dist[j]
                nextIndex = j
        print(nextIndex)
        visit[nextIndex] = True
        for j in range(vertex_num):
            if dist[j] > graph[nextIndex][j] and not visit[j]:
                dist[j] = graph[nextIndex][j]
                preindex[j] = nextIndex
    return dist, preindex


def prim_dict(graph, root):
    assert type(graph) == dict
    nodes = list(graph.keys())
    nodes.remove(root)
    visited = [root]
    path = []
    next = None
    while nodes:
        distance = float('inf')
        for s in visited:
            for d in graph[s]:
                if d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    pre = s
                    next = d
        path.append((pre, next))
        visited.append(next)
        nodes.remove(next)
    return path


if __name__ == '__main__':
    _ = 1 << 10
    graph = [
        [0, 6, 3, _, _, _],
        [6, 0, 2, 5, _, _],
        [3, 2, 0, 3, 4, _],
        [_, 5, 3, 0, 2, 3],
        [_, _, 4, 2, 0, 5],
        [_, _, _, 3, 5, 0],
    ]
    prim(graph, 6)

    graph_dict = {"s1": {"s1": 0, "s2": 2, "s10": 3, "s12": 4, "s5": 3},
                  "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2, "s5": 2},
                  "s10": {"s1": 2, "s2": 6, "s10": 0, "s12": 3, "s5": 4},
                  "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0, "s5": 2},
                  "s5": {"s1": 3, "s2": 5, "s10": 2, "s12": 4, "s5": 0},
                  }
    path = prim_dict(graph_dict, 's12')
    print(path)
