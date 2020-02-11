N = int(input())
record = {}
for _ in range(N):
    num, score = list(map(int, input().strip().split()))
    if num not in record:
        record[num] = score
    else:
        record[num] += score
# record_st = sorted(record.items(), key=lambda x: x[1])
# print(record_st[-1][0], record_st[-1][1])
max_val = 0
max_key = 0
for key, val in record.items():
    if val > max_val:
        max_key = key
        max_val = val
print(max_key, max_val)