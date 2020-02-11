a = [i for i in input().strip().split()]
A, B = "", ""
for i in a[0]:
    if i == a[1]:
        A += i
for i in a[2]:
    if i == a[3]:
        B += i
if A == "":
    A = "0"
if B == "":
    B = "0"
print(int(A) + int(B), end='')