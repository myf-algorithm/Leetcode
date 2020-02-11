a = input()
sum = 0
res = []
for c in a:
    # sum += int(c)
    sum += (ord(c) - ord('0'))

for c in str(sum):
    if c == '0':
        res.append('ling')
    elif c == '1':
        res.append('yi')
    elif c == '2':
        res.append('er')
    elif c == '3':
        res.append('san')
    elif c == '4':
        res.append('si')
    elif c == '5':
        res.append('wu')
    elif c == '6':
        res.append('liu')
    elif c == '7':
        res.append('qi')
    elif c == '8':
        res.append('ba')
    elif c == '9':
        res.append('jiu')
print(' '.join(res))
