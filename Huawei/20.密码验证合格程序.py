import sys

res = []

while True:
    input = sys.stdin.readline().strip()
    if input == '':
        break
    xc_flag = 0
    dc_flag = 0
    num_flag = 0
    else_flag = 0
    chuan_flag = 0
    for c in input:
        if 'a' <= c and c <= 'z':
            xc_flag = 1
        elif 'A' <= c and c <= 'Z':
            dc_flag = 1
        elif '0' <= c and c <= '9':
            num_flag = 1
        else:
            else_flag = 1
    for i in range(len(input) - 5):
        if input.count(input[i:i + 3]) > 1:
            chuan_flag = 1
    if len(input) > 8 and (xc_flag + dc_flag + num_flag + else_flag) >= 3 and chuan_flag == 0:
        res.append('OK')
    else:
        res.append('NG')

for r in res:
    print(r)
