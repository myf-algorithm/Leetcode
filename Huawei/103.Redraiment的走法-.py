import sys


def GetResult(n, pInput, pResult):
    pResult.append(0)
    temp = [1 for index in range(n)]
    for index in range(1, n):
        cnt = 0
        i = index
        while i > 0:
            i = i - 1
            if pInput[index] > pInput[i] and cnt < temp[i]:
                cnt = temp[i]
        temp[index] = cnt + 1
    pResult[0] = max(temp)


while True:
    n = sys.stdin.readline().strip()
    if n:
        n = int(n)
        num = [int(v) for v in sys.stdin.readline().strip().split(' ')]
        pResult = []
        GetResult(n, num, pResult)
        print(pResult[0])
    else:
        break

import bisect

while True:
    try:
        a, b = int(input()), map(int, input().split())
        q = []
        for v in b:
            pos = bisect.bisect_left(q, v)
            if pos == len(q):
                q.append(v)
            else:
                q[pos] = v
        print(len(q))
    except:
        break
