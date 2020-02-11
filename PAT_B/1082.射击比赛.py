def main():
    N = int(input())
    maxx = -1
    minn = 101 * 101 * 2
    first = ''
    last = ''
    for index in range(N):
        ID, x, y = (int(z) for z in input().split())
        if x * x + y * y > maxx:
            maxx = x * x + y * y
            last = "{:0>4d}".format(ID)
        if x * x + y * y < minn:
            minn = x * x + y * y
            first = "{:0>4d}".format(ID)
    print(first, last)


if __name__ == '__main__':
    main()
