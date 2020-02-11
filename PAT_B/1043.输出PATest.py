a = input()
s = "PATest"
count = [0 for i in range(6)]
for i in range(6):
    count[i] = a.count(s[i])
res = ''
while not (count[0] == 0 and count[1] == 0 and count[2] == 0 and count[3] == 0 and count[4] == 0 and count[5] == 0):
    for i in range(6):
        if count[i] != 0:
            res += s[i]
            count[i] -= 1
print(res)
