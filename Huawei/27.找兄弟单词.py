from collections import defaultdict

while True:
    try:
        dd = defaultdict(list)
        a = input().split()
        words, lookup, num, brothers = a[1:1 + int(a[0])], a[-2], int(a[-1]), []
        for i in words:
            dd["".join(sorted(i))].append(i)
        for i in dd["".join(sorted(lookup))]:
            if i != lookup:
                brothers.append(i)
        print(len(brothers))
        if brothers and num <= len(brothers):
            print(sorted(brothers)[num - 1])
    except:
        break
