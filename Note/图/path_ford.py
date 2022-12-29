# Bellman-Ford算法可以非常好的解决带有负权的最短路径问题，什么是负权？
# 如果两个顶点之间的距离为正数，那这个距离成为正权。
# 反之，如果一个顶点到一个顶点的距离为负数，那这个距离就称为负权。
# Bellman-Ford和Dijkstra 相似，都是采用‘松弛’的方法来寻找最短的距离


def getEdges(G):
    """ 读入图G，返回其边与端点的列表 """
    v1 = []  # 出发点
    v2 = []  # 对应的相邻到达点
    w = []  # 顶点v1到顶点v2的边的权值
    for i in G:
        for j in G[i]:
            if G[i][j] != 0:
                w.append(G[i][j])
                v1.append(i)
                v2.append(j)
    return v1, v2, w


def Bellman_Ford(G, v0, INF=999):
    v1, v2, w = getEdges(G)
    # 初始化源点与所有点之间的最短距离
    dis = dict((k, INF) for k in G.keys())
    dis[v0] = 0
    # 核心算法
    for k in range(len(G) - 1):  # 循环 n-1轮
        check = 0  # 用于标记本轮松弛中dis是否发生更新
        for i in range(len(w)):  # 对每条边进行一次松弛操作
            if dis[v1[i]] + w[i] < dis[v2[i]]:
                dis[v2[i]] = dis[v1[i]] + w[i]
                check = 1
        if check == 0: break
    # 检测负权回路
    # 如果在 n-1 次松弛之后，最短路径依然发生变化，则该图必然存在负权回路
    flag = 0
    for i in range(len(w)):  # 对每条边再尝试进行一次松弛操作
        if dis[v1[i]] + w[i] < dis[v2[i]]:
            flag = 1
            break
    if flag == 1:
        return False
    return dis


if __name__ == '__main__':
    graph_dict = {"s1": {"s1": 0, "s2": 2, "s10": 3, "s12": 4, "s5": 3},
                  "s2": {"s1": 1, "s2": 0, "s10": 4, "s12": 2, "s5": 2},
                  "s10": {"s1": 2, "s2": 6, "s10": 0, "s12": 3, "s5": 4},
                  "s12": {"s1": 3, "s2": 5, "s10": 2, "s12": 0, "s5": 2},
                  "s5": {"s1": 3, "s2": 5, "s10": 2, "s12": 4, "s5": 0},
                  }
    dis = Bellman_Ford(graph_dict, 's1')
    print(dis)
