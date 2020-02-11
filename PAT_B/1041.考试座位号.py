N = int(input())
information = {}
for _ in range(N):
    num, kao, zuo = list(map(int, input().strip().split()))
    information[kao] = [num, zuo]
M = int(input())
for i in list(map(int, input().strip().split())):
    print("%d %d" %(information[i][0], information[i][1]))
