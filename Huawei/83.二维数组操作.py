while True:
    try:
        col, index = map(int, input().strip().split(' '))
        x1, y1, x2, y2 = map(int, input().strip().split(' '))
        new_col = int(input().strip())
        new_index = int(input().strip())
        findx, findy = map(int, input().strip().split(' '))
        if col <= 9 and index <= 9:
            print('0')
        else:
            print('-1')
        if x1 < col and y1 < index and x2 < col and y2 < index:
            print('0')
        else:
            print('-1')
        if new_col < col:
            print('0')
        else:
            print('-1')
        if new_index < index:
            print('0')
        else:
            print('-1')
        if findx < col and findy < index:
            print('0')
        else:
            print('-1')
    except:
        break
