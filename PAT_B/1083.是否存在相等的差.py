N = int(input())
data = [int(x) for x in input().split()]
chas = {}
for index, _ in enumerate(data):
    temp = abs(data[index] - index - 1)
    chas.setdefault(temp, 0)
    chas[temp] += 1
indexs = sorted(chas, reverse=True)
for x in indexs:
    if chas[x] > 1:
        print("{} {}".format(x, chas[x]))
