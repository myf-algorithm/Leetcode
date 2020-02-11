s = input().strip()
count = {}
for c in s:
    if c not in count:
        count[c] = 1
    else:
        count[c] += 1
if len(count) > 1:
    for i in count:
        if count[i] == min(count.values()):
            s = s.replace(i, "")
print(s)

# from collections import defaultdict
# while True:
#     try:
#         a = input()
#         dd = defaultdict(int)
#         for i in a:
#             dd[i] += 1
#         for i in dd:
#             if dd[i] == min(dd.values()):
#                 a = a.replace(i, "")
#         print(a)
#     except:
#         break
