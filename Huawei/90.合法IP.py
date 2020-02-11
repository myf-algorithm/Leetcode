while True:
    try:
        IPV4 = input().strip().split('.')
        flag = 0
        if len(IPV4) == 4:
            for i in IPV4:
                try:
                    b32 = int(i)
                    if not 0 <= b32 <= 255:
                        flag = 1
                        break
                except:
                    flag = 1
                    break
        if flag == 1:
            print('NO')
        else:
            print('YES')
    except:
        break
