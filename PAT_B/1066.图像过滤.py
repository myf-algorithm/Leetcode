n = input().split()
for i in range(int(n[0])):
    m = input().split()
    for j in range(int(n[1])):
        if int(n[2]) <= int(m[j]) <= int(n[3]):
            m[j] = n[4].zfill(3)
        else:
            m[j] = m[j].zfill(3)
    print(' '.join(m))
