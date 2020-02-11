n = input()
a = []
import math

for i in range(int(n)):
    x = input().split()
    a.append(math.sqrt(int(x[0]) ** 2 + int(x[1]) ** 2))
print('%.2f' % max(a))
