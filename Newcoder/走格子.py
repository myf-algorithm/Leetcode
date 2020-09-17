# coding:utf-8
import collections


def shortestPath(grid, k, a, b, c, d):
    m, n = len(grid), len(grid[0])
    if m == 1 and n == 1:
        return 0

    k = min(k, m + n - 3)
    visited = set([(0, 0, k)])
    q = collections.deque([(0, 0, k)])

    step = 0
    while len(q) > 0:
        cnt = len(q)
        for _ in range(cnt):
            x, y, rest = q.popleft()
            for dx, dy, dt in [(-1, 0, a), (1, 0, b), (0, -1, c), (0, 1, d)]:
                step += dt
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 'o' and (nx, ny, rest) not in visited:
                        if nx == m - 1 and ny == n - 1:
                            return step
                        q.append((nx, ny, rest))
                        visited.add((nx, ny, rest))
                    elif grid[nx][ny] == 'x' and rest > 0 and (nx, ny, rest - 1) not in visited:
                        q.append((nx, ny, rest - 1))
                        visited.add((nx, ny, rest - 1))
    return -1


# coding:utf-8
import sys

# n为节点数，m为边数
T = int(sys.stdin.readline().strip())
res = []
for _ in range(T):
    lines = sys.stdin.readline().strip()
    n, m = list(map(int, lines.split()))
    lines = sys.stdin.readline().strip()
    x, y = list(map(int, lines.split()))
    lines = sys.stdin.readline().strip()
    a, b, c, d = list(map(int, lines.split()))
    in_map = []
    for _ in range(n):
        lines = sys.stdin.readline()
        in_map.append(list(lines.strip()))
    print(in_map)
    res.append(shortestPath(in_map, 0, a, b, c, d))
# print(res)
for i in range(len(res)):
    if i == -1:
        print('Case #' + str(i + 1) + ': ' + str(-1))
    else:
        print('Case #' + str(i + 1) + ': ' + str(res[i]))
