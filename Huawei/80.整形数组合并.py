while True:
    try:
        a, b, c, d = input(), list(map(int, input().split())), input(), list(map(int, input().split()))
        print("".join(map(str, sorted(list(set(b + d))))))
    except:
        break
