while True:
    try:
        a, b, c = input(), map(int, input().split()), input()
        print(" ".join(map(str, sorted(b))) if c == "0" else " ".join(map(str, sorted(b, reverse=True))))
    except:
        break
