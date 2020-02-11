n, m = list(map(int, input().split()))

for i in range(n):  # 每组分数
    score_lst = input().split()
    g2 = int(score_lst[0])
    con = 0
    max, min = 0, m
    sum = 0.0

    for i in range(1, n):  # 每个分数筛选、统计
        s = int(score_lst[i])
        if s in range(0, m + 1):
            con += 1
            sum += s
            if s < min:
                min = s
            if s > max:
                max = s
    sum = sum - min - max
    g1 = sum / (con - 2)
    score = (g1 + g2) / 2
    if g1 == int(g1):
        if score != int(score):
            score = int(score) + 1
    print("%.f" % score)
