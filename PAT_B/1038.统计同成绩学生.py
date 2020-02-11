N = int(input())
score = list(map(int, input().strip().split()))
K = list(map(int, input().strip().split()))
grade = [0 for i in range(101)]
for i in score:
    grade[i] += 1
res = []
for i in K[1:]:
    res.append(str(grade[i]))
print(' '.join(res))
