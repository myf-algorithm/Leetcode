while True:
    try:
        a, res = int(input()), 0
        for i in range(7, a + 1):
            if "7" in str(i) or i % 7 == 0:
                res += 1
        print(res)
    except:
        break