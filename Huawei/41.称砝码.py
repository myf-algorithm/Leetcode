# 没啥技巧，穷举法，关键代码就几行。。。注意算法复杂度。
import sys

try:
    while True:
        number = sys.stdin.readline().strip()
        line_1 = sys.stdin.readline().strip()
        line_2 = sys.stdin.readline().strip()
        if number == '' or line_1 == '' or line_2 == '':
            break
        line_1 = line_1.split()
        line_2 = line_2.split()
        line_1 = [int(x) for x in line_1]
        line_2 = [int(x) for x in line_2]
        mylist = []
        for j in range(int(number)):
            s = 0
            m = len(mylist)
            for k in range(0, line_2[j] + 1):
                mylist.append(s)
                for i in range(m):
                    mylist.append(mylist[i] + s)
                s += line_1[j]
            mylist = list(set(mylist))
        myset = set(mylist)
        print(len(myset))
except:
    pass
