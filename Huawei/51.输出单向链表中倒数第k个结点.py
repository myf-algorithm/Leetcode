while True:
    try:
        a, b, c = input(), input().split(), int(input())
        print(b[-c] if c != 0 else 0)
    except:
        break