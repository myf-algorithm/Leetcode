num_str, s = list(map(str, input().strip().split()))
num = int(num_str)
ceng = 1
cur = 1
if num == 1:
    ceng = 1
    num = 0
    print(s)
else:
    num -= 1
    cur += 2
    while True:
        if num >= cur * 2:
            num -= cur * 2
            cur += 2
            ceng += 1
        else:
            break
    for i in range(ceng):
        print(' ' * i, end='')
        print(s * (2 * (ceng - i) - 1))
    for i in range(ceng - 1):
        print(' ' * (ceng - 2 - i), end='')
        print((s * (2 * (i + 2) - 1)))
print(num)
