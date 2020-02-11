n = int(input())
res_dict = {}
level_dict = {
    "B": 2 / 3,
    "A": 1,
    "T": 1.5
}
for _ in range(n):
    numb, score, school = input().split()
    school_key = school.lower()
    res_dict[school_key] = res_dict.get(school_key, [0, 0])
    school_list = res_dict[school_key]
    school_list[1] += 1
    school_list[0] += level_dict.get(numb[0]) * int(score)

res_list = []

for key, vals in res_dict.items():
    res_list.append([int(vals[0]), vals[1], key])
res_list.sort(key=lambda x: [-x[0], x[1], x[2]])

print(len(res_dict))
score = -1
rank = 0
for ix, ls in enumerate(res_list, 1):
    if ls[0] != score:
        rank = ix
        score = ls[0]
    print(u"%d %s %d %d" % (rank, ls[2], ls[0], ls[1]))
