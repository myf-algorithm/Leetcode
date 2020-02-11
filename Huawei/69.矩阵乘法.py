try:
    while True:
        x = input()
        x = int(x)
        y = input()
        y = int(y)
        z = input()
        z = int(z)
        res = [[0 for i in range(z)] for j in range(x)]
        m1 = []
        for i in range(x):
            m1.append(list(map(int, input().split())))
        m2 = []
        for i in range(y):
            m2.append(list(map(int, input().split())))
        for i in range(x):
            for j in range(z):
                he = 0
                for k in range(y):
                    he += m1[i][k] * m2[k][j]
                res[i][j] = he
        for i in res:
            print(' '.join(map(str, i)))
except:
    pass
