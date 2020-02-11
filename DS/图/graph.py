# 图的术语：
# G=(V,E)，有向图和无向图
# 邻接点：边的两个顶点为邻接点，这条边为邻接边
# 完全图：任意两个顶点之间有边连接的图为完全图：
#       无向完全图：n * n * (n - 1) / 2个边
#       有向完全图：n * n * (n - 1)个边
# 度：连接顶点的边数，有向图分出度和入度
# 路径：顶点的路径
# 环：起点和终点一样的路径
# 连通图（任何来那个顶点都是连通的），强连通有向图
# 连通子图，极大连通子图


# 邻接矩阵存储，无向图
class MGraph(object):
    def __init__(self, edges, directed=False):
        self.directed = directed
        self.edges = edges
        self.vertex = []
        self.vnum = 0
        self.edges_mat = []
        self.init_vertex(edges)
        self.init_edge_mat(edges)

    def init_vertex(self, edges):
        vertex = []
        # 遍历所有边，统计顶点
        for edge in edges:
            if edge[0] not in vertex:
                vertex.append(edge[0])
            if edge[1] not in vertex:
                vertex.append(edge[1])
        self.vertex = vertex
        self.vnum = len(vertex)

    def init_edge_mat(self, edges):
        zeros_mat = []
        for i in range(self.vnum):
            zeros_mat.append([0 for i in range(self.vnum)])
        # 使用一个方阵存储边
        for edge in edges:
            u, v = self.vertex.index(edge[0]), self.vertex.index(edge[1])
            zeros_mat[u][v] = 1
            if not self.directed:
                zeros_mat[v][u] = 1
        self.edges_mat = zeros_mat


# 使用邻接表表示。每个顶点的邻接点构成一个线性表，使用单链表存储
# 有向图：
#       以顶点为起点，邻接表
#       以顶点为终点，逆邻接表
class GraphAL(object):
    def __init__(self, edges, directed=False):
        self.directed = directed
        self.edges = edges
        self.vertex = []
        self.vnum = 0
        self.adj_list = []
        self.init_vertex(edges)
        self.init_adj_list(edges)

    def init_vertex(self, edges):
        vertex = []
        # 遍历所有的边，统计顶点
        for edge in edges:
            if edge[0] not in vertex:
                vertex.append(edge[0])
            if edge[1] not in vertex:
                vertex.append(edge[1])
        self.vertex = vertex
        self.vnum = len(vertex)

    def init_adj_list(self, edges):
        adj_list = []
        for i in range(self.vnum):
            adj_list.append([])
        # 建立邻接表
        for edge in edges:
            u, v = self.vertex.index(edge[0]), self.vertex.index(edge[1])
            adj_list[u].append(v)
            if not self.directed:
                adj_list[v].append(u)
        self.adj_list = adj_list

    def get_vertex(self):
        return self.vertex

    def get_adj_list(self):
        return self.adj_list

    def get_edges(self):
        return self.edges


# DFS，深度优先搜索，得到DFS序列
# n个顶点，e条边
# 采用邻接矩阵：O(n*n)
# 采用邻接表：O(n+e)
def dep_traverse(graph, v0):
    vertex = graph.get_vertex()
    not_visited = vertex.copy()
    adj_list = graph.get_adj_list()

    def _traverse(v):
        if v not in not_visited:
            return
        else:
            print(v)
            not_visited.remove(v)
            v_adj = adj_list[vertex.index(v)]
            if len(v_adj) > 0:
                _traverse(vertex[v_adj[0]])

    while len(not_visited) > 0:
        _traverse(v0)
        if len(not_visited) > 0:
            v0 = not_visited[0]


# BFS，广度优先搜索，得到BFS序列
def bfs_traverse(graph, v0):
    vertex = graph.get_vertex()
    not_visited = vertex.copy()
    adj_list = graph.get_adj_list()
    while len(not_visited) > 0:
        if v0 not in not_visited:
            return
        if v0 in not_visited:
            print(v0)
            not_visited.remove(v0)
        v_adj = adj_list[vertex.index(v0)]
        for i in v_adj:
            if vertex[i] in not_visited:
                print(vertex[i])
                not_visited.remove(vertex[i])
        if len(not_visited) > 0:
            v0 = not_visited[0]


if __name__ == '__main__':
    g = GraphAL([(1, 2), (3, 2), (6, 7)])
    dep_traverse(g, 0)
    bfs_traverse(g, 1)
