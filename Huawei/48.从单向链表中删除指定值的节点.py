try:
    while True:
        s = input().split()
        num = int(s[0])
        res = [s[1]]
        for i in range(num - 1):
            a = s[2 + i * 2]
            b = s[3 + i * 2]
            res.insert(res.index(b) + 1, a)
        rm = s[-1]
        res.remove(rm)
        print(' '.join(res) + ' ')
except:
    pass
