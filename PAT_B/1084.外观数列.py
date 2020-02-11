d, n = input().split()
for _ in range(1, int(n)):
    des = ""
    l = len(d)
    ix = 0
    while ix < l:
        char = d[ix]
        cn = 1
        while ix + 1 < l and d[ix + 1] == char:
            ix = ix + 1
            cn += 1
        des += char
        des += str(cn)
        ix += 1
    d = des

print(d)
