from collections import Counter

while True:
    try:
        a, b, c, d, invalid = input(), input().split(), input(), input().split(), 0
        cc = Counter(d)
        for i in b:
            print(i + " : " + str(cc[i]))
            invalid += cc[i]
        print("Invalid : " + str(len(d) - invalid))
    except:
        break
