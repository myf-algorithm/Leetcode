import math


def isPrime(k):
    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True


def group_lst(lst):  # 分奇偶
    odd = []
    even = []
    for i in lst:
        if int(i) % 2 == 1:
            odd.append(int(i))
        else:
            even.append(int(i))
    return (odd, even)


def matrix_ab(a, b):
    matrix = [[0 for i in range(len(b))] for i in range(len(a))]
    for ii, i in enumerate(a):
        for jj, j in enumerate(b):
            if isPrime(i + j) == True:
                matrix[ii][jj] = 1
    return matrix


def find(x):
    for index, i in enumerate(b):
        if matrix[x][index] == 1 and used[index] == 0:
            used[index] = 1
            if connect[index] == -1 or find(connect[index]) != 0:
                connect[index] = x
                return 1
    return 0


while True:
    try:
        n = int(input())
        m = input().split()
        (a, b) = group_lst(m)
        matrix = matrix_ab(a, b)
        connect = [-1 for i in range(len(b))]
        count = 0
        for i in range(len(a)):
            used = [0 for j in range(len(b))]
            if find(i):
                count += 1
        print(count)
    except:
        break
