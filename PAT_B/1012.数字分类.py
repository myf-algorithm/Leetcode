a = [int(i) for i in input().strip().split()][1:]
A1 = []
A2 = []
A3 = []
A4 = []
A5 = []
res = []
for i in a:
    if (i % 5 == 0) and (i % 2 == 0):
        A1.append(i)
    if i % 5 == 1:
        A2.append(i)
    if i % 5 == 2:
        A3.append(i)
    if i % 5 == 3:
        A4.append(i)
    if i % 5 == 4:
        A5.append(i)
if len(A1) == 0:
    res.append('N')
else:
    res.append(str(sum(A1)))
if len(A2) == 0:
    res.append('N')
else:
    for i in range(len(A2)):
        if i % 2 == 1:
            A2[i] *= -1
    res.append(str(sum(A2)))
if len(A3) == 0:
    res.append('N')
else:
    res.append(str(len(A3)))
nsum = 0
if len(A4) == 0:
    res.append('N')
else:
    for i in A4:
        nsum += i
    res.append(str(round(nsum / len(A4), 1)))
if len(A5) == 0:
    res.append('N')
else:
    res.append(str(max(A5)))
print(' '.join(res))
