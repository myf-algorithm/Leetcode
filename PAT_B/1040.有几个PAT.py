a = list(input())
a.reverse()
count_T = 0
count_AT = 0
count_PAT = 0
for i in a:
    if i == 'T':
        count_T += 1
    elif i == 'A':
        count_AT = (count_AT + count_T) % 1000000007
    else:
        count_PAT = (count_PAT + count_AT) % 1000000007
print(count_PAT)
