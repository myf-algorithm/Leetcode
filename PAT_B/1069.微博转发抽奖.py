n = input().split()
a = []
b, c = int(n[1]), int(n[2])
flag = 0
d = []
for i in range(1, int(n[0]) + 1):
    a.append(input())
    if (i - c) % b == 0 and i >= c:
        if not a[i - 1] in d:
            print(a[i - 1])
            d.append(a[i - 1])
            flag = 1
        else:
            c += 1
if flag == 0:
    print("Keep going...")
