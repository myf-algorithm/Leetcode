# coding:utf-8
# 深信服1,9.24
import sys

# 组数
T = int(input())

# 结果
res = []

for _ in range(T):
    lines = sys.stdin.readline().strip()
    A, B, N = list(map(int, lines.split()))
    lines = sys.stdin.readline().strip()
    Record = list(map(int, lines.split()))
    if B > N:
        res.append('No')
        continue
    end = int(N) - int(B) + 1
    for i in range(end):
        if i == end - 1 and Record[i + B - 1] - Record[i] + 1 > A:
            res.append('No')
            break
        if Record[i + B - 1] - Record[i] + 1 <= A:
            res.append('Yes')
            break



for i in res:
    print(i)