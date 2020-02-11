def logi(a, b):
    if a > b:
        print(" Gai", end="")
    elif a == b:
        print(" Ping", end="")
    else:
        print(" Cong", end="")


UInput = input()
UInput = UInput.split()
UInput = list(map(int, UInput))
for j in range(99, 9, -1):
    y = (j % 10) * 10 + j // 10
    b = (abs(j - y)) / UInput[1]
    if b * UInput[2] == y:
        print(j, end="")
        logi(UInput[0], j)
        logi(UInput[0], y)
        logi(UInput[0], b)
        break
else:
    print("No Solution")
