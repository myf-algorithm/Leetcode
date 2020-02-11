n = input().split()
m = input().split()
a = int(n[0])
b = int(n[1])
m1 = m[a - b:]
m2 = m[:a - b]
x = m1 + m2
print(' '.join(x))