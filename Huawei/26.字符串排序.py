a = [i for i in input()]
b = []
for c in a:
    if c.isalpha():
        b.append(c)
d = sorted([(c.lower(), c) for c in b], key=lambda x: x[0])
e = [c[1] for c in d]
count = 0
for i in range(len(a)):
    if a[i].isalpha():
        a[i] = e[count]
        count += 1
out = ""
for c in a:
    out += c
print(out)

# def f(s):
#     a, L = [], len(s)
#     for i in range(L):
#         if s[i].isalpha():
#             a.append((s[i], s[i].lower(), i))
#     b = sorted(a, key=lambda x: (x[1], x[2], x[0]))
#     result = ''
#     for i in range(L):
#         if s[i].isalpha():
#             result += b[0][0]
#             del b[0]
#         else:
#             result += s[i]
#     return result
# try:
#     while 1:
#         print(f(input()))
# except:
#     pass
