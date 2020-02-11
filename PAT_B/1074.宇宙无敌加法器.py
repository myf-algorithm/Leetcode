l = [int(x) for x in list(input())]
n1 = [int(x) for x in list(input().rjust(len(l), '0'))]
n2 = [int(x) for x in list(input().rjust(len(l), '0'))]

for i in range(len(l)):
    if l[i] == 0:
        l[i] = 10

rst = [0]
k = -1
j = 0
while k >= -len(l):
    if n1[k] + n2[k] + j >= l[k]:
        num = n1[k] + n2[k] + j - l[k]
        j = 1
        rst.insert(0, j)
    else:
        num = n1[k] + n2[k] + j
        j = 0
        rst.insert(0, j)
    rst[1] = num
    k -= 1
rst = [str(x) for x in rst]
print(int(''.join(rst)))
