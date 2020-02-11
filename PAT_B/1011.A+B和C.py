T = int(input())
for i in range(T):
    num = input().strip().split()
    if int(num[0]) + int(num[1]) > int(num[2]):
        print("Case #%d: true" % (i + 1))
    else:
        print("Case #%d: false" % (i + 1))
