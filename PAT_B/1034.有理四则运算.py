# 整理出两个数化简形式
def f(a, b):
    fac = b
    while a % fac:
        r = a % fac
        a = fac
        fac = r
    return fac


def lst(x):
    if x[0] == '-':
        lst_x = [-1]
        a, b = x[1:].split('/')
    else:
        lst_x = [1]
        a, b = x.split('/')
    a, b = int(a), int(b)
    fac = f(a, b)
    a = a // fac
    b = b // fac
    lst_x.append(a)
    lst_x.append(b)
    return lst_x


# 输出打印形式 最简形式
def print_x(num):
    if num[1] == 0 or num[2] == 0:
        return '0'
    lst = [num[0]]
    lst.append(num[1] // num[2])
    a = num[1] % num[2]
    b = num[2]
    fac = f(a, b)
    a = a // fac
    b = b // fac
    lst.append(a)
    lst.append(b)

    str_x = ''
    if lst[1] == 0:
        if lst[2] != 0:
            str_x += str(lst[2])
            str_x += '/'
            str_x += str(lst[3])
    else:
        str_x += str(lst[1])
        if lst[2] == 0:
            pass
        else:
            str_x += ' '
            str_x += str(lst[2])
            str_x += '/'
            str_x += str(lst[3])
    if lst[0] == -1:
        str_x = '(-%s)' % str_x
    return str_x


# 有理数的加减乘除运算，参数a, b 的格式为[ -1 , 3, 2]
def sum_(a, b):
    a1 = a[0] * a[1] * b[2]
    b1 = b[0] * b[1] * a[2]
    r = a1 + b1
    if r < 0:
        ret = [-1]
        r *= -1
    else:
        ret = [1]
    ret.append(r)
    ret.append(a[2] * b[2])
    return ret


def sub_(a, b):
    c = b.copy()
    c[0] = c[0] * (-1)
    ret = sum_(a, c)
    return ret


def mul_(a, b):
    ret = [a[0] * b[0]]
    ret.append(a[1] * b[1])
    ret.append(a[2] * b[2])
    return ret


def div_(a, b):
    b[1], b[2] = b[2], b[1]
    ret = mul_(a, b)
    return ret


if __name__ == '__main__':
    x, y = input().split()
    lst_x = lst(x)
    lst_y = lst(y)
    x = print_x(lst_x)
    y = print_x(lst_y)

    r1 = print_x(sum_(lst_x, lst_y))
    r2 = print_x(sub_(lst_x, lst_y))
    r3 = print_x(mul_(lst_x, lst_y))
    r4 = print_x(div_(lst_x, lst_y))
    if y == '0':
        r4 = 'Inf'

    print(x, '+', y, '=', r1)
    print(x, '-', y, '=', r2)
    print(x, '*', y, '=', r3)
    print(x, '/', y, '=', r4)
