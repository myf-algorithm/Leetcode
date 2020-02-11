while True:
    try:
        from collections import defaultdict

        a = input()
        d = defaultdict(int)
        b = []
        for x in a:
            if x in d:
                d[x] = d[x] + 1
            else:
                d[x] = 1
        for x in d:
            if d[x] == 1:
                b.append(x)
        b = sorted(b, key=a.index)
        if b:
            print(b[0])
        else:
            print('-1')
    except:
        break
