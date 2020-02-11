num = input()
num_list = [int(i) for i in num]
res = ""
if len(num_list) == 3:
    res += num_list[0] * 'B' + num_list[1] * 'S'
    if num_list[2] != 0:
        tmp = ""
        for i in range(num_list[2]):
            tmp += str(i + 1)
        res += tmp

if len(num_list) == 2:
    res += num_list[0] * 'S'
    if num_list[1] != 0:
        tmp = ""
        for i in range(num_list[1]):
            tmp += str(i + 1)
        res += tmp

if len(num_list) == 1:
    if num_list[0] != 0:
        tmp = ""
        for i in range(num_list[0]):
            tmp += str(i + 1)
        res += tmp
print(res)

