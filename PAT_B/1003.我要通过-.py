import re

n = input()
for i in range(int(n)):
    s = input()
    if re.match(r'A*PA+TA*', s):  # 在字符串中进行匹配
        a = re.split(r'[P|T]', s)  # 以字符P, T进行分段
        if a[0] * len(a[1]) == a[2]:  # 条件判断
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
