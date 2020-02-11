def main():
    n = input()
    n = n.split()
    Check = {}
    flag = True
    for i in range(int(n[0])):
        temp = input()
        temp = temp.split()
        if temp[0] in Check:
            Check[temp[0]] = Check[temp[0]] + " " + temp[1]
        else:
            Check[temp[0]] = temp[1]
        if temp[1] in Check:
            Check[temp[1]] = Check[temp[1]] + " " + temp[0]
        else:
            Check[temp[1]] = temp[0]
    for i in range(int(n[1])):
        temp = input()
        temp = temp.split()
        for j in range(1, len(temp)):
            if temp[j] not in Check:
                continue
            temp2 = Check[temp[j]]
            temp2 = temp2.split()
            for k in range(1, len(temp)):
                if temp[k] in temp2:
                    flag = False
                    break
            if not flag:
                print("No")
                break
        if flag:
            print("Yes")
        else:
            flag = True


main()
