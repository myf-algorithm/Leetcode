n = int(input())
A = [0] * (n + 1)
for i in range(1, n + 1):
    A[i] = int(input())

sw = bw = 0
for i in range(1, n):  # 遍历认定两个人做狼
    for j in range(i + 1, n + 1):
        lieh = liew = 0
        for k in range(1, n + 1):
            if A[k] < 0 and -A[k] != i and -A[k] != j or A[k] > 0 and (A[k] == i or A[k] == j):  # 有人说了谎
                if k != i and k != j:  # 好人说谎
                    lieh += 1
                else:  # 狼人说谎
                    liew += 1
        if liew == 1 and lieh == 1:
            sw, bw = i, j
            break
    if sw:
        break

if sw:
    print("{} {}".format(sw, bw))
else:
    print("No Solution")
