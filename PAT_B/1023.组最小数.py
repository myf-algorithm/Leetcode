a = list(map(int, input().strip().split()))
num = ""
for i in range(len(a)):
    num += a[i] * str(i)
num_lt = [int(i) for i in num]
num_st = sorted(num_lt)
num_rm = num_st.copy()
res = ""
if 0 in num_st:
    while 0 in num_rm:
        num_rm.remove(0)
    a = num_rm[0]
    num_st.remove(a)
    res += str(a)
    for i in num_st:
        res += str(i)
else:
    for i in num_st:
        res += str(i)
print(res, end='')
