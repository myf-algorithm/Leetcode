c = input()
d = input()


def transfer(a):
    n = len(a) // 8 + 1 if len(a) > 8 else 1
    m = len(a) % 8

    for i in range(n):
        if i == n - 1:
            if m:
                print(a[-m:] + '0' * (8 - m))
        else:
            print(a[i * 8: i * 8 + 8])


transfer(c)
transfer(d)

