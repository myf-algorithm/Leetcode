while True:
    try:
        n = list(input().strip())
        num = 0
        if len(n) != 0:
            for i in n:
                if i.isupper():
                    num += 1
            print(num)
        else:
            print(num)
    except:
        break
