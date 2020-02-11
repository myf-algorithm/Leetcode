while True:
    try:
        c_list = input().strip()
        list1 = [i for i in c_list.split(' ')]
        num = len(list1)
        print(num)
        for i in list1:
            print(i)
    except:
        break
