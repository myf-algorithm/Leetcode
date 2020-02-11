N = int(input())
values = set()
for x in range(1, N + 1):
    values.add(int(x / 2) + int(x / 3) + int(x / 5))
print(len(values))
