a, b = input().split('E')
fu = a[0]
zheng, xiao = a[1:].split('.')
zhi_fu, zhi_shu = b[0], b[1:]
res = ""
if zhi_fu == '-':
    if len(zheng) > int(zhi_shu):
        zheng_lt = [i for i in zheng]
        zheng_lt.insert(len(zheng) - int(zhi_shu), '.')
        zheng = ''.join(zheng_lt)
        if fu == '-':
            res += '-'
            res += zheng
            res += xiao
        elif fu == '+':
            res += zheng
            res += xiao
    elif len(zheng) <= int(zhi_shu):
        if fu == '-':
            res += '-'
            res += '0.'
            res += '0' * (int(zhi_shu) - len(zheng))
            res += zheng
            res += xiao
        elif fu == '+':
            res += '0.'
            res += '0' * (int(zhi_shu) - len(zheng))
            res += zheng
            res += xiao
elif zhi_fu == '+':
    if len(xiao) > int(zhi_shu):
        xiao_lt = [i for i in xiao]
        xiao_lt.insert(int(zhi_shu), '.')
        xiao = ''.join(xiao_lt)
        if fu == '-':
            res += '-'
            res += zheng
            res += xiao
        elif fu == '+':
            res += zheng
            res += xiao
    elif len(xiao) <= int(zhi_shu):
        if fu == '-':
            res += '-'
            res += zheng
            res += xiao
            res += '0' * (int(zhi_shu) - len(xiao))
        elif fu == '+':
            res += zheng
            res += xiao
            res += '0' * (int(zhi_shu) - len(xiao))
print(res)
