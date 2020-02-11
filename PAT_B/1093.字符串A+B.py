l = input() + input()
s = set(l)
for i in l:
    if i in s:
        s.remove(i)
        print(i, end='')
