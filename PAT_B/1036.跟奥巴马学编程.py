import math
N, s = list(map(str, input().strip().split()))
if int(N) / 2 - math.floor(int(N) / 2) == 0.5:
    row = math.floor(int(N) / 2) + 1
else:
    row = math.floor(int(N) / 2)
print(s * int(N))
for _ in range(row - 2):
    print(s + ' ' * (int(N) - 2) + s)
print(s * int(N))
