a1_lt = [i for i in input()]
a2_lt = [i for i in input()]
for i in a2_lt:
    if i in a1_lt:
        a1_lt.remove(i)
a1_lt_upper = [i.upper() for i in a1_lt]
res = []
for i in a1_lt_upper:
    if i not in res:
        res.append(i)
print("".join(res))
