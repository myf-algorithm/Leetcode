while True:
    try:
        n = int(input())
        res = [['' for i in range(n)] for j in range(n)]
        count = 1
        for i in range(n):
            for j in range(i + 1):
                res[i - j][j] = str(count)
                count += 1
        for i in range(n):
            while '' in res[i]:
                res[i].remove('')
            print(' '.join(res[i]))
    except:
        break

