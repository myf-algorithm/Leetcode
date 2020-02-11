while True:
    try:
        data = input()
        max_l = 0
        for i in range(len(data) - 1):
            if data[i] == data[i + 1]:
                if max_l == 0:
                    max_l = 2
                x = 1
                while i - x >= 0 and i + 1 + x < len(data) and data[i - x] == data[i + 1 + x]:
                    if max_l < 2 * (x + 1):
                        max_l = 2 * (x + 1)
                    x = x + 1
            if i >= 0 and data[i - 1] == data[i + 1]:
                y = 1
                while i - y > 0 and i + y < len(data) and data[i - y] == data[i + y]:
                    if max_l < 2 * y + 1:
                        max_l = 2 * y + 1
                    y = y + 1
        print(max_l)
    except:
        break
