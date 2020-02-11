def solver(board, rows, cols, squs, i, j):
    if i >= 9:
        return True

    if board[i][j] != '0':
        return solver(board, rows, cols, squs, (i * 9 + j + 1) // 9, (i * 9 + j + 1) % 9)

    for n in {'1', '2', '3', '4', '5', '6', '7', '8', '9'} - (rows[i] | cols[j] | squs[i // 3 * 3 + j // 3]):
        board[i][j] = n
        rows[i].add(n)
        cols[j].add(n)
        squs[i // 3 * 3 + j // 3].add(n)

        if not solver(board, rows, cols, squs, (i * 9 + j + 1) // 9, (i * 9 + j + 1) % 9):
            board[i][j] = '0'
            rows[i].remove(n)
            cols[j].remove(n)
            squs[i // 3 * 3 + j // 3].remove(n)
        else:
            return True
    return False


while True:
    try:
        board = []
        for i in range(9):
            board.append(input().split())

        rows, cols, squs = [set() for i in range(9)], [set() for i in range(9)], [set() for i in range(9)]
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != '0':
                    rows[i].add(num)
                    cols[j].add(num)
                    squs[i // 3 * 3 + j // 3].add(num)
        solver(board, rows, cols, squs, 0, 0)
        for i in range(9):
            print(' '.join(board[i]))
    except:
        break
