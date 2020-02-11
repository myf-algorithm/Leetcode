n = int(input())
stu = {}
for i in range(n):
    message = input().strip().split()
    item = message[0] + ' ' + message[1]
    stu[item] = int(message[2])
stu_order = sorted(stu.items(), key=lambda x: x[1], reverse=True)
print(stu)
print(stu_order[0][0])
print(stu_order[-1][0])
