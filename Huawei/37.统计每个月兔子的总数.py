while True:
    try:
        a = int(input()) - 1
        arr = [1, 2]
        while len(arr) < a:
            arr.append(arr[-1] + arr[-2])
        print(arr[-1])
    except:
        break
