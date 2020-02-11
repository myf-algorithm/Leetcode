while True:
    try:
        D = {'3': 0, '4': 1, '5': 2, '6': 3, '7': 4, '8': 5, '9': 6, '10': 7, 'J': 8, 'Q': 9, 'K': 10, 'A': 11, '2': 12,
             'joker': 13, 'JOKER': 14}
        a, b = input().split('-')
        s1, s2 = a.split(), b.split()
        if a == 'joker JOKER' or b == 'joker JOKER':
            print('joker JOKER')
        elif len(s1) == len(s2):
            print(a if D[s1[0]] > D[s2[0]] else b)
        elif len(a) == 7:
            print(a)
        elif len(b) == 7:
            print(b)
        else:
            print('ERROR')
    except:
        break
