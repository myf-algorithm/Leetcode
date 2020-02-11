while True:
    try:
        up, down = list(map(int, input().split("/")))
        res = ""
        while up != 1:
            if down % (up - 1) == 0:
                res += "1/" + str(down // (up - 1)) + "+"
                up = 1
            else:
                res += "1/" + str(down // up + 1) + "+"
                x = up - down % up
                down = down * (down // up + 1)
                up = x
                if down % up == 0:
                    down = down // up
                    up = 1
        res += "1/" + str(int(down))
        print(res)
    except:
        break
