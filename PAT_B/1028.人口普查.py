n = int(input())
count = 0
max1 = ['', '2014/09/06']
min1 = ['', '1814/09/06']
for i in range(n):
    person = input().split()
    if '1814/09/06' <= person[1] <= '2014/09/06':
        count += 1
        if person[1] < max1[1]:
            max1 = person
        if person[1] > min1[1]:
            min1 = person

if count == 0:
    print('0')
else:
    print(count, max1[0], min1[0])