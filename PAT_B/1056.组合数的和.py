input_num = input().split()
n = input_num[0]
input_num = list(map(int, input_num[1:]))
sum_nums = 0
for i in input_num:
    for j in input_num:
        if i == j:
            continue
        num = i * 10 + j
        sum_nums += num
print(sum_nums)
