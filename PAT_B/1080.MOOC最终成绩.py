def get_dict(n):
    d = dict()
    for _ in range(n):
        stu_id, score = input().split()
        d[stu_id] = int(score)
    return d


def get_score(d, l):
    for i in range(len(l)):
        if l[i][0] in d.keys():
            l[i].append(d[l[i][0]])
        else:
            l[i].append(-1)
    return l


n1, n2, n3 = [int(x) for x in input().split()]
p = get_dict(n1)
mid = get_dict(n2)
final = get_dict(n3)
tmp = list()

for stu_id, score in p.items():
    if score >= 200:
        tmp.append([stu_id, score])

tmp = get_score(mid, tmp)
tmp = get_score(final, tmp)
rst = list()

for stu in tmp:
    if stu[2] > stu[3]:
        g = int(stu[2] * 0.4 + stu[3] * 0.6 + 0.5)
    else:
        g = stu[3]
    stu.append(g)
    if g >= 60:
        rst.append(stu)

rst.sort(key=lambda x: x[0], reverse=False)
rst.sort(key=lambda x: x[4], reverse=True)

for i in rst:
    i = [str(x) for x in i]
    print(' '.join(i))
