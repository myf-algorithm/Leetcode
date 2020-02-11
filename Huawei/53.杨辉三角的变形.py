def getIndex(n):
    matrix = [[0 for j in range(2 * n - 1)] for i in range(n)]
    matrix[0][n - 1] = 1
    for i in range(1, n):
        for j in range(1, 2 * n - 2):
            matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][j + 1]
    matrix[n - 1][0] = 1
    matrix[n - 1][2 * n - 2] = 1
    for k in range(2 * n - 2):
        if matrix[n - 1][k] % 2 == 0:
            return k + 1
    return -1


while True:
    try:
        n = int(input())
        print(getIndex(n))
    except:
        break