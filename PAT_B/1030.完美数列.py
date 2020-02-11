N, p = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
a_s = sorted(a)
m = 0
for i in range(len(a_s)):
    if i + m > N:
        break
    for j in range(i + m, len(a_s)):
        if a_s[j] > p * a_s[i]:  # 如果不满足完美数列条件，直接break
            break
        m += 1  # 优化的地方
print(m)
