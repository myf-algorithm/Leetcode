# coding:utf-8
import sys

# n为节点数，m为边数
lines = sys.stdin.readline().strip()
n, m = list(map(int, lines.split()))

# m个边的连接和时间
edges = []
for i in range(m):
    lines = sys.stdin.readline().strip()
    edges.append(list(map(int, lines.split())))

# 起点，终点，出发时间
lines = sys.stdin.readline().strip()
s, e, start = list(map(str, lines.split()))
s, e = int(s), int(e)
start_month, start_day = list(map(int, start.split('/')[0].split('.')))
start_hour = int(start.split('/')[1])

# 无向图最短路径算法
used = [False for _ in range(n)]
distance = [float('inf') for _ in range(n)]
cost = [[float('inf') for _ in range(n)] for _ in range(n)]


def dijkstra(s):
    distance[s] = 0
    while True:
        v = -1
        for u in range(n):
            if not used[u] and (v == -1 or distance[u] < distance[v]):
                v = u
        if v == -1:
            break
        used[v] = True
        for u in range(n):
            distance[u] = min(distance[u], distance[v] + cost[v][u])


if __name__ == '__main__':
    for i in range(m):
        v, u, w = edges[i]
        cost[v - 1][u - 1] = w
    dijkstra(s - 1)
    need_hour = distance[e - 1]
    day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    need_day = start_day + (start_hour + need_hour) // 24
    need_hour = (start_hour + need_hour) % 24

    while True:
        if need_day > day_list[start_month - 1]:
            need_day -= day_list[start_month - 1]
            start_month += 1
        else:
            break

    res = ''
    res += str(start_month) + '.' + str(need_day) + '/' + str(need_hour)
    print(res)

# 4 4
# 1 2 250
# 1 3 180
# 2 4 280
# 3 4 220
# 1 4 7.30/8
