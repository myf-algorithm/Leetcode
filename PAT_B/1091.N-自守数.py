input()
for i in input().split(' '):
    inti = int(i)
    ii = inti ** 2
    m = 10 ** len(i)
    flag = True
    j = 1
    while (j < 10):
        if ((ii * j) % m - inti == 0):
            flag = False
            break
        else:
            j += 1
    if (flag):
        print('No')
    else:
        print(j, ii * j)
