m = input()
n = input()
str1 = ''
for i in n:
    if 'a' <= i <= 'z':
        s = i.upper()
    else:
        s = i
    if s not in m:
        if '+' not in m or (i < 'A' or i > 'Z'):
            str1 += i
print(str1)
