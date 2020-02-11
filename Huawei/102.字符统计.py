while True:
    try:
        string = str(input())
        d = {}
        for s in string:
            if s.isdigit() or s.isalpha() or s == ' ':
                if s in d.keys():
                    d[s] += 1
                else:
                    d[s] = 1
        d2 = sorted(sorted(d.items(), key=lambda x: x[0]), key=lambda item: item[1], reverse=True)
        str1 = ''.join([k for (k, v) in d2])
        print(str1)
    except:
        break
