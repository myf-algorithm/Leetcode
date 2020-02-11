# -*- coding: utf-8 -*-
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
num = '0123456789'
numberList = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
integralUnit = ['元', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿', '拾', '佰', '仟']
fractionUnit = ['角', '分']


def tran(x):
    o = ''
    index = 0
    for i in range(len(x) - 1, -1, -1):
        o = numberList[num.find(x[i])] + integralUnit[index] + o
        index += 1
    if '拾' in o and '元' in o:
        if o[len(o) - 2] == '零':
            o = o[:len(o) - 2] + o[len(o) - 1]
    if '拾' in o and '万' in o:
        if o.find('万') > 2 and o[o.find('万') - 2] == '拾' and o[o.find('万') - 1] == '零':
            o = o[:o.find('万') - 1] + o[o.find('万'):]
    if '拾' in o and '亿' in o:
        if o.find('亿') > 2 and o[o.find('亿') - 2] == '拾' and o[o.find('亿') - 1] == '零':
            o = o[:o.find('亿') - 1] + o[o.find('亿'):]
    i = 0
    out = ''
    while i < len(o):
        if o[i] == '零':
            if out[len(out) - 1] != '零':
                out += '零'
            i += 2
        else:
            out += o[i]
            i += 1
    o = ''
    for i in range(len(out)):
        if out[i] == '零' and (out[i + 1] == '亿' or out[i + 1] == '万' or out[i + 1] == '元'):
            continue
        else:
            o += out[i]
    out = ''
    for i in range(len(o)):
        if o[i] == '壹':
            if o[i + 1] == '拾':
                continue
            else:
                out += o[i]
        else:
            out += o[i]
    return out


def tranf(x):
    o = ''
    if x[0] != '0':
        o = numberList[num.find(x[0])] + fractionUnit[0]
    if x[1] != '0':
        o += numberList[num.find(x[1])] + fractionUnit[1]
    return o


o = '人民币'
try:
    while True:
        s = input()
        s = float(s)
        if s.is_integer():
            s = int(s)
            s = str(s)
            print(o + tran(s) + '整')
        else:
            s = str(s)
            z, f = map(str, s.split('.'))
            f = f + (2 - len(f)) * '0'
            if z != '0':
                print(o + tran(z) + tranf(f))
            else:
                print(o + tranf(f))
except:
    pass