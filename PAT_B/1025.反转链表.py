link = [None] * 100000
head, N, K = map(int, input().split(' '))
for i in range(N):
    add, data, next = map(int, input().split(' '))
    link[add] = [data, next]
T, p = [], head
while -1 != p:
    if not link[p]:
        break
    T.append(["%05d" % (p), link[p][0]])
    p = link[p][1]
for j in range(K - 1, len(T), K):
    i = j - K + 1
    while i < j:
        T[i], T[j] = T[j], T[i]
        i += 1
        j -= 1
T.append(['-1'])
for i in range(len(T) - 1):
    print("%s %d %s" % (T[i][0], T[i][1], T[i + 1][0]))
