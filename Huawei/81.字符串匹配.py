while True:
    try:
        a, b = input(), input()
        flag = 0
        for i in a:
            if i not in b:
                flag = 1
                break
            else:
                flag = 0
        if flag == 1:
            print('false')
        else:
            print('true')
    except:
        break
