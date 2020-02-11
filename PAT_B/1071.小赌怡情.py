l = list(map(int, input().split()))
x, n = l[0], l[1]
for i in range(n):
    l = list(map(int, input().split()))
    if x < l[2]:
        print('Not enough tokens.  Total = {0}.'.format(x))
    elif (l[0] - l[3]) * (l[1] - 0.5) > 0:
        x -= l[2]
        print('Lose {0}.  Total = {1}.'.format(l[2], x))
    elif (l[0] - l[3]) * (l[1] - 0.5) < 0:
        x += l[2]
        print('Win {0}!  Total = {1}.'.format(l[2], x))
    if x == 0:
        print('Game Over.')
        break
