while True:
    try:
        nums = int(input())
        cmds = input()
        cur, begin = 1, 1
        for cmd in cmds:
            if cmd == 'D':
                cur += 1
                if cur > nums:
                    cur = begin = 1
                if cur - begin > 3:
                    begin += 1
            else:
                cur -= 1
                if cur == 0:
                    cur = nums
                    begin = nums - 3
                if cur < begin:
                    begin -= 1
        if nums < 4:
            l = list(range(1, nums + 1))
            song = ''
            for i in l:
                song += str(i) + " "
            print(song)
        else:
            song = ''
            l = list(range(begin, begin + 4))
            song = ''
            for i in l:
                song += str(i) + " "
            print(song)
        print(cur)
    except:
        break
