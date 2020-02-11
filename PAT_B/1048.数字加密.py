a, b = list(map(str, input().strip().split()))
a = a[::-1]
b = b[::-1]
res = ""
s = ['J', 'Q', 'K']
if len(a) >= len(b):
    m = len(a)
    f = len(a) - len(b)
    b += '0' * f
else:
    m = len(b)
    f = len(b) - len(a)
    a += '0' * f
for i in range(m):
    if i % 2 == 0:
        num = (int(a[i]) + int(b[i])) % 13
        if 0 <= num <= 9:
            res += str(num)
        else:
            res += s[num - 10]
    else:
        num = int(b[i]) - int(a[i])
        if num < 0:
            num += 10
            res += str(num)
        else:
            res += str(num)
print(res[::-1])
