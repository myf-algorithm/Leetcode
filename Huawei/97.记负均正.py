while True:
    try:
        a, nums, pos, neg = int(input()), map(int, input().split()), [], 0
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg += 1
        print(str(neg) + " 0" if not pos else str(neg) + " " + "{0:.1f}".format(sum(pos) / len(pos)))
    except:
        break
