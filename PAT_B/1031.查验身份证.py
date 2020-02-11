N = int(input())
weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
M = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
num_flag = 0
no_flag = 0
for _ in range(N):
    a = input()
    num_flag = 0
    sum = 0
    for i in range(17):
        if '0' <= a[i] <= '9':
            sum += int(a[i]) * weight[i]
        else:
            num_flag = 1
            no_flag = 1
            print(a)
            break
    if num_flag == 0:
        if M[sum % 11] != a[-1]:
            no_flag = 1
            print(a)
if no_flag == 0:
    print("All passed")
