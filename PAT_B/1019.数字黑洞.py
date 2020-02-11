def padding(N):
    i = ""
    if 0 <= int(N) < 10:
        i += "000"
        for c in N:
            i += c
    elif 10 <= int(N) < 100:
        i += "00"
        for c in N:
            i += c
    elif 100 <= int(N) < 1000:
        i += "0"
        for c in N:
            i += c
    elif 1000 <= int(N) < 10000:
        for c in N:
            i += c
    return i


def list_str(s):
    s1 = ""
    for i in s:
        s1 += i
    return s1


# N = input()
# while int(N) != 6174 and int(N) != 0:
#     a = list_str(sorted(padding(N), reverse=True))
#     b = list_str(sorted(padding(N)))
#     c = int(a) - int(b)
#     if c == 0 or c == 6174:
#         print("%s - %s = %s" % (a, b, padding(str(c))), end='')
#     else:
#         print("%s - %s = %s" % (a, b, padding(str(c))))
#     N = str(c)


str_ = input()
ret = "{0:0>4}".format(str_)
if len(set(ret)) == 1:
    print("%s - %s = 0000" % (ret, ret))
else:
    while True:
        num_lt = list(map(int, ret))
        num1 = sorted(num_lt, reverse=True)
        num2 = sorted(num_lt)
        str1 = "".join(list(map(str, num1)))
        str2 = "".join(list(map(str, num2)))
        ret = "{0:0>4}".format(int(str1) - int(str2))
        print("{0:0>4} - {1:0>4} = {2}".format(str1, str2, ret))
        if ret == "6174":
            break

