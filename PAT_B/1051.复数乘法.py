import math

r1, p1, r2, p2 = list(map(float, input().strip().split()))
a1, b1, a2, b2 = r1 * math.cos(p1), r1 * math.sin(p1), r2 * math.cos(p2), r2 * math.sin(p2)
r = a1 * a2 - b1 * b2
i = a1 * b2 + b1 * a2

if -0.005 <= r < 0:
    print('0.00', end='')
else:
    print('%.2f' % r, end='')

if i >= 0:
    print('+%.2fi' % i)
elif -0.005 <= i < 0:
    print('+0.00i')
elif i < 0:
    print('%.2fi' % i)
