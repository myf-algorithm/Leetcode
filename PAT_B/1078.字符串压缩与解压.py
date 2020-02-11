pro = input()
string = input()
n = len(string)
ans = ""  # 输出结果
if pro == "C":  # 压缩
    i = 0
    while i < n:  # 从i 开始寻找连续相同的字符，计数为con
        j = i + 1
        con = 1
        while j < n and string[j] == string[i]:
            con += 1
            j += 1
        if con == 1:  # 计数为1 则直接加到ans
            ans = ans + string[i]
        else:
            new = "%d%s" % (con, string[i])
            ans = ans + new
        i = j  # i 定位到下一个字符

else:  # 解压
    i = 0
    while i < n:
        j = i + 1
        if string[i].isdigit():  # 从i 开始寻找连续的数字字符，为数量num
            while string[j].isdigit():
                j += 1
            num = int(string[i:j])
            new = string[j] * num
            ans = ans + new
            i = j + 1
        else:  # 若i 不为数字，直接添加到ans
            ans = ans + string[i]
            i = j
print(ans)
