def perfectNum(n):
    count = 0
    for i in range(3, n + 1):
        temp = 0
        r = i // 2 if i % 2 == 0 else (i + 1) // 2
        for j in range(2, r + 1):
            if i % j == 0:
                temp += j
        if temp + 1 == i:
            count += 1
    return count


while True:
    try:
        n = int(input())
        print(perfectNum(n))
    except:
        break