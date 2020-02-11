s = list(map(int, input()))
N = list(set(s))
for i in range(len(N)):
    print("%d:%d" % (N[i], s.count(N[i])))


