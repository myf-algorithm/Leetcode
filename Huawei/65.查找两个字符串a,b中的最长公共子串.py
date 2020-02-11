while True:
    try:
        a = input()
        b = input()
        if len(a) > len(b):
            temp = a
            a = b
            b = temp
        str_m = ''
        for i in range(len(a)):
            for j in range(i, len(a)):
                temp = a[i:j + 1]
                if b.find(temp) < 0:
                    break
                elif len(str_m) < len(temp):
                    str_m = temp
        print(str_m)
    except:
        break
