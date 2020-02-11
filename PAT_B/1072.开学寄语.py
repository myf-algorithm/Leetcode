N, M = map(int, input().split(" "))
list1 = input().split(" ")
dict1 = {}
people = 0
things = 0
for i in range(N):
    ipt_list = input().split(" ")
    for j in ipt_list[2:]:
        if j in list1 and ipt_list[0] not in dict1.keys():
            dict1[ipt_list[0]] = j
            people += 1
            things += 1
        elif ipt_list[0] in dict1.keys() and j in list1:
            dict1[ipt_list[0]] = dict1[ipt_list[0]] + " " + j
            things += 1
for k, v in dict1.items():
    print("%s: %s" % (k, v))
print(people, things)
