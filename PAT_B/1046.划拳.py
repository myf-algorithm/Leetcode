N = int(input())
count1 = 0
count2 = 0
for _ in range(N):
    a = list(map(int, input().strip().split()))
    if a[0] + a[2] == a[1] and a[0] + a[2] != a[3]:
        count2 += 1
    if a[0] + a[2] != a[1] and a[0] + a[2] == a[3]:
        count1 += 1
print(count1, count2)