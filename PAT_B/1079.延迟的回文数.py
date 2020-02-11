num = input()
cn = 0
sum_ab = num
while cn <= 10:
    a = sum_ab
    b = a[::-1]
    if a == b:
        print('%s is a palindromic number.' % sum_ab)
        break
    if cn == 10:
        print('Not found in 10 iterations.')
        break
    sum_ab = str(int(a) + int(b))
    print(a, '+', b, '=', sum_ab)
    cn += 1
