a = list(map(str, input().strip()))
b = list(map(str, input().strip()))
flag = 0
count = 0
for i in b:
    if i in a:
        a.remove(i)
    else:
        flag = 1
        count += 1
if flag == 0:
    print("Yes %d" % (len(a)))
else:
    print("No %d" % (count))
