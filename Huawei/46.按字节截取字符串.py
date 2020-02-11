while True:
    try:
        a, b = input().split()
        print(a[:int(b)])
    except:
        break
