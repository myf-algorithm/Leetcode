n = int(input())
a = input().split()
error = []
right = []
for i in a:
    try:
        k = int(i)
        if k < -1000 or k > 1000:
            error.append(i)
        else:
            right.append(k)
    except:
        try:
            k = float(i)
            if k < -1000 or k > 1000:
                error.append(i)
            elif len(i) - i.index('.') - 1 > 2:
                error.append(i)
            else:
                right.append(k)
        except:
            error.append(i)
for i in range(len(error)):
    print("%s%s%s" % ("ERROR: ", error[i], " is not a legal number"))
if len(right) == 0:
    print("%s%d%s" % ("The average of ", len(right), " numbers is Undefined"))
elif len(right) == 1:
    print("%s%d%s%.2f" % ("The average of ", len(right), " number is ", right[0]))
else:
    b = 0
    for i in right:
        b += i
    b = b / len(right)
    print("%s%d%s%.2f" % ("The average of ", len(right), " numbers is ", b,))
