num_N, num_M = input().split()
num_N, num_M = int(num_N), int(num_M)

value_list, error_list, answer_list = [], [], []
# 输入各个多选题的情况

for i in range(num_M):
    error_list.append(0)
    string = input().split()
    value_list.append(string[0])
    answer_list.append(string[2:])


# 得到学生的答案情况
for i in range(num_N):
    sum = 0
    string = input()
    string = string[1:-1]
    string = string.split(') (')
    for j in range(num_M):
        my = ' '.join(answer_list[j])
        if my == string[j]:
            sum += int(value_list[j])
        else:
            error_list[j] += 1
    print(sum)

max_value = max(error_list)
if max_value == 0:
    print("Too simple")
else:
    print(max_value, end='')
    for i in range(num_M):
        if error_list[i] == max_value:
            print(' ' + str(i + 1), end="")

