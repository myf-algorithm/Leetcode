n = int(input())
a = [int(i) for i in input().split()]
a.sort(reverse=True)
E = 0
for i in range(n):
    if a[i] > E + 1:
        E += 1
print(E)
