import sys

while True:
    try:
        string = sys.stdin.readline()
        int(string)
        for i in range(101):
            for j in range(101 - i):
                for k in range(101 - i - j):
                    if 15 * i + 9 * j + k == 300 and i + j + k == 100:
                        print(i, j, k)
    except:
        break
