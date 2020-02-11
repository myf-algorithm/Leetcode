while True:
    try:
        y = 0
        out = ''
        x = int(input())
        for i in range(x):
            y = y + 2 * i
        z = int((x ** 3 - y) / x - 2)
        for j in range(x):
            z = z + 2
            out = out + str(z) + '+'
        print(out[0:len(out) - 1])
    except:
        break
