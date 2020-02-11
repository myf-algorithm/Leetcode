N = int(input())
a = list(map(float, input().strip().split()))
ans = 0.0
for i in range(N):
    ans += a[i] * (i + 1) * (N - i)
print('%.2f' % ans)
