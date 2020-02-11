op = ['+', '-', '*', '/']


def f(ls, op):
    for i in range(4):
        for j in range(4):
            if i != j:
                for o in op:
                    res = '(' + ls[i] + o + ls[j] + ')'
                    for k in range(4):
                        if k != i and k != j:
                            for o in op:
                                res = '(' + res + o + ls[k] + ')'
                                for l in range(4):
                                    if l != i and l != j and l != k:
                                        for o in op:
                                            r = eval(res + o + ls[l])
                                            if abs(r - 24) <= 0.001:
                                                return 'true'
    return 'false'


while True:
    try:
        ls = input().split()
        print(f(ls, op))
    except:
        break
