from collections import Counter

while True:
    try:
        a = int(input())
        for i in range(a):
            c, start, res = Counter(input()), 26, 0
            for j in c.most_common():
                res += j[1] * start
                start -= 1
            print(res)
    except:
        break