while True:
    try:
        res, a = 0, bin(int(input())).replace("0b", "")
        for i in range(1, len(a) + 1):
            if "1" * i in a:
                res = i
            else:
                break
        print(res)
    except:
        break
