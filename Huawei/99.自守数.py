while True:
    try:
        a, res = int(input()), 0
        for i in range(0, a + 1):
            if str(i ** 2).endswith(str(i)):
                res += 1
        print(res)
    except:
        break