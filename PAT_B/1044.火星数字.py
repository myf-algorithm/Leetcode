x = ['tret', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']
y = ['', 'tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']


def earth(num):
    y_ = num // 13
    x_ = num % 13
    if y_ == 0:
        print(x[x_])
    else:
        if x_ == 0:
            print(y[y_])
        else:
            print(y[y_], x[x_])


def huo(string):
    lst = string.split()
    if len(lst) == 1:
        if lst[0] in x:
            num = x.index(lst[0])
        else:
            num = y.index(lst[0]) * 13
        print(num)
    else:
        y_, x_ = lst[0], lst[1]
        num = y.index(y_) * 13 + x.index(x_)
        print(num)


n = eval(input())
for i in range(n):
    string = input()
    if string.isdigit():
        earth(int(string))
    else:
        huo(string)
