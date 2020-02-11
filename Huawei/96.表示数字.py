while True:
    try:
        a, res, isNum = input(), "", False
        for i in a:
            if i.isdigit():
                if not isNum:
                    res = res + "*" + i
                else:
                    res += i
                isNum = True
            else:
                if isNum:
                    res = res + "*" + i
                else:
                    res += i
                isNum = False
        if a[-1].isdigit():
            res += "*"
        print(res)
    except:
        break
