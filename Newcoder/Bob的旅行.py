# encoding:utf-8
import sys

# N个星球
N = int(sys.stdin.readline().strip())

# N行时间和位置
Pos = []
for i in range(N):
    lines = sys.stdin.readline().strip()
    Pos.append(list(map(int, lines.split())))

V = []
for i in range(len(Pos[1:])):
    dt = (Pos[i][0] - Pos[i - 1][0])
    dx = (Pos[i][1] - Pos[i - 1][1])
    dy = (Pos[i][2] - Pos[i - 1][2])
    dz = (Pos[i][3] - Pos[i - 1][3])
    v = ((dx * dx) + (dy * dy) + (dz * dz)) / dt
    V.append(v)


inx = 0
max_cur = 0
for i in range(len(V)):
    if V[i] > max_cur:
        max_cur = V[i]
        inx = i
print(inx)