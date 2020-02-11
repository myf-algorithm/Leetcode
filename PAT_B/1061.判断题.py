number = input().split()
score = input().split()
rans = input().split()
for i in range(int(number[0])):
    sum = 0
    stu = input().split()
    for j in range(len(stu)):
        if stu[j] == rans[j]:
            sum += int(score[j])
    print(sum)
