while True:
    try:
        s = input()
        max_length, temp_length = 0, 0
        index_start, index_end = 0, 0
        res = ''
        for i in range(len(s)):
            if (i == 0 and s[i].isdigit()) or (s[i].isdigit() and s[i - 1].isdigit() == False):
                index_start = i
            if (i > 1 and s[i].isdigit() == False and s[i - 1].isdigit()) or (s[i].isdigit() and (i + 1) == len(s)):
                index_end = i
                if s[i].isdigit():
                    temp_length = index_end - index_start + 1
                else:
                    temp_length = index_end - index_start
                if max_length < temp_length:
                    max_length = temp_length
                    res = s[index_start:index_start + max_length]
                elif max_length == temp_length:
                    res += s[index_start:index_start + max_length]
        print("%s,%d" % (res, max_length))
    except:
        break
