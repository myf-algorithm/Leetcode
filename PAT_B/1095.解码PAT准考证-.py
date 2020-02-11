n, m = map(int, input().split(" "))
ipt_list = []
for i in range(n):
    ipt = input().split(" ")
    ipt_list.append(ipt)
que_list = []
for i in range(m):
    dict1 = {}
    ipt = input().split(" ")
    if ipt[0] == "1":
        for j in ipt_list:
            if j[0][0] == ipt[1]:
                dict1[j[0]] = int(j[1])
        print("Case %d: %s" % (i + 1, " ".join(ipt)))
        if dict1 == {}:
            print("NA")
        else:
            dict1_list = sorted(dict1.items(), key=lambda a: (-a[1], a[0]))
            for k in dict1_list:
                print(k[0], k[1])
    elif ipt[0] == "2":
        sum1 = 0
        count = 0
        for j in ipt_list:
            if j[0][1:4] == ipt[1]:
                sum1 += int(j[1])
                count += 1
        print("Case %d: %s" % (i + 1, " ".join(ipt)))
        if count == 0:
            print("NA")
        else:
            print(count, sum1)
    else:
        dict2 = {}
        for j in ipt_list:
            if j[0][4:10] == ipt[1]:
                if j[0][1:4] not in dict2.keys():
                    dict2[j[0][1:4]] = 1
                else:
                    dict2[j[0][1:4]] += 1
        print("Case %d: %s" % (i + 1, " ".join(ipt)))
        if dict2 == {}:
            print("NA")
        else:
            dict2_list = sorted(dict2.items(), key=lambda a: (-a[1], a[0]))
            for k in dict2_list:
                print(k[0], k[1])
