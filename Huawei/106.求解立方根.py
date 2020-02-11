import math
while True:
    try:
        num = float(input())
        num2 = math.pow(num, 1.0/3)
        print('%.1f' % num2)
    except:
        break