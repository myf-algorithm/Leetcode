n, k = list(map(int, input().strip().split()))
lst = []

for i in range(n):
    name, height = input().split()
    lst.append([int(height), name])

lst.sort(key=lambda x: (-x[0], x[1]))  # 排序，若多人身高相同，则按名字的字典序升序排列。
n_per_row = n // k
n_lastrow = n - n_per_row * (k - 1)
person_eachrow = [lst[:n_lastrow]] + [lst[n_lastrow + n_per_row * i:n_lastrow + n_per_row * (i + 1)] for i in
                                      range(k - 1)]

for pers in person_eachrow:
    length = len(pers)
    ret = ['' for i in range(length)]
    mid = length // 2
    ret[mid] = pers[0][1]
    cn = 1
    for j in range(1, length, 2):
        if j == length - 1:
            ret[mid - cn] = pers[j][1]
        else:
            ret[mid - cn] = pers[j][1]
            ret[mid + cn] = pers[j + 1][1]
            cn += 1
    print(" ".join(ret))
