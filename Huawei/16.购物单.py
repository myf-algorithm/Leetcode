while True:
    try:
        N, m = map(int, input().strip().split())
        a = [[0] * (N + 1) for i in range(m + 1)]
        goods = []
        for i in range(m):
            goods.append(list(map(int, input().strip().split())))
        for i in range(1, m + 1):
            for j in range(1, N + 1):
                if goods[i - 1][2] == 0:  # 表示是主件
                    if goods[i - 1][0] <= j:  # <=j表示买的起可以有选择, 这时候有两种选择，可以买也可以不买，选择最优的方案
                        a[i][j] = max(a[i - 1][j], a[i - 1][j - goods[i - 1][0]] + goods[i - 1][1] * goods[i - 1][0])
                        # a[i][j] 表示用j元钱去买i件物品的最优解（这里就是（价格和重要性乘积）最大值）
                else:
                    if goods[i - 1][0] + goods[goods[i - 1][2] - 1][0] <= j:  # 要买附件的话，必须先买主件，所以必须有能买两件的钱
                        a[i][j] = max(a[i - 1][j],
                                      a[i - 1][j - goods[i - 1][0]] + goods[i - 1][0] * goods[i - 1][1],
                                      a[i - 1][j - goods[i - 1][0] - goods[goods[i - 1][2] - 1][0]] + goods[i - 1][0] *
                                      goods[i - 1][1] + goods[goods[i - 1][2] - 1][0] * goods[goods[i - 1][2] - 1][1])
        print(max([max(row) for row in a]))  # 这时候矩阵右下角并不是最大值，需要求整个矩阵的最大值
    except:
        break
