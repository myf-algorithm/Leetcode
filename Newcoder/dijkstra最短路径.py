# _*_ encoding:utf-8 _*_

V = 7
used = [False for _ in range(V)]
distance = [float('inf') for _ in range(V)]
cost = [[float('inf') for _ in range(V)] for _ in range(V)]


def dijkstra(s):
    distance[s] = 0
    while True:
        v = -1
        for u in range(V):
            if not used[u] and (v == -1 or distance[u] < distance[v]):
                v = u
        if v == -1:
            break
        used[v] = True
        for u in range(V):
            distance[u] = min(distance[u], distance[v] + cost[v][u])


if __name__ == '__main__':
    for _ in range(4):
        v, u, w = list(map(int, input().split()))
        cost[v][u] = w
    s = int(input('请输入一个起始点：'))
    dijkstra(s)
    print(distance)
