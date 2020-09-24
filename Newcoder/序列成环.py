# coding:utf-8
# 深信服2,9.24
import sys

# 组数
T = int(input())

# 结果
res = []

for _ in range(T):
    N = int(input())
    lines = sys.stdin.readline().strip()
    Record = list(map(int, lines.split()))
    if N == 1:
        res.append(0)
        break
    if N == 2 and Record == [1, 2]:
        res.append(2)
        break
    if N == 2 and Record == [2, 1]:
        res.append(0)
        break
    Gold = list(range(2, N + 1)) + [1]
    count = 0
    for i in range(N):
        if Record[i] != Gold[i]:
            count += 1
    res.append(count)
for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i], end='')
    else:
        print(res[i])
