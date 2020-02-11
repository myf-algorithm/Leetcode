n = eval(input())
import re

wifi = [0 for i in range(n)]
wifi_ = "ABCD"
for i in range(n):
    ans = input()
    pa = re.compile(r'[A-D]-T')
    m = re.search(pa, ans)
    ans_num = m.group()
    wifi[i] = wifi_.index(ans_num[0]) + 1
    print(wifi[i], end="")
