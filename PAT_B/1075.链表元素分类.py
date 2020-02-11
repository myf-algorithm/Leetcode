f_address, N, K = input().split(" ")
K = int(K)
N = int(N)
all_list = []
for i in range(N):
    ipt_list = input().split(" ")
    ipt_list[1] = int(ipt_list[1])
    all_list.append(ipt_list)
all_list1 = []
all_list2 = []
all_list3 = []
while 1:
    if all_list == []:
        break
    for i in all_list:
        if i[0] == f_address:
            if i[1] < 0:
                i[1] = str(i[1])
                all_list1.append(i)
            elif 0 <= i[1] <= K:
                i[1] = str(i[1])
                all_list2.append(i)
            else:
                i[1] = str(i[1])
                all_list3.append(i)
            f_address = i[2]
            all_list.remove(i)
sort_all_list = all_list1 + all_list2 + all_list3
sort_all_list[N - 1][2] = "-1"
a = sort_all_list[N - 1][0]
for i in range(N - 2, -1, -1):
    sort_all_list[i][2] = a
    a = sort_all_list[i][0]
for i in sort_all_list:
    print(" ".join(i))
