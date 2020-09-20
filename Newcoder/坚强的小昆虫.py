# _*_ encoding:utf-8 _*_
# 9.20 度小满笔试1
import sys

T = int(input())
res = []


def caculate(map_in):

    return -1


for _ in range(T):
    lines = sys.stdin.readline().strip()
    N, M = list(map(int, lines.split()))
    map_in = []
    for i in range(N):
        lines = sys.stdin.readline().strip()
        map_in.append(list(map(str, lines.split())))
    res.append(caculate(map_in))

for i in res:
    print(i)
