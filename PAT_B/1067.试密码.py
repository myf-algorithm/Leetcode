password, n = input().split(" ")
n = int(n)
for i in range(n):
    ipt = input()
    if ipt == "#":
        break
    if ipt == password:
        print("Welcome in")
        break
    else:
        if i == n - 1:
            print("Wrong password: %s" % ipt)
            print("Account locked")
            break
        else:
            print("Wrong password: %s" % ipt)
