# _*_ encoding:utf-8 _*_
# 9.20 度小满笔试2

# 时间限制： 5000MS
# 内存限制： 655360KB
# 题目描述：
# 你的实验室中诞生了一种新的无性繁殖生物，这种生物每一个都有且仅有一个父亲（注意，其中有且仅有1号生物的父亲无法追踪到了）。为了研究方便，你定义一个生物的1级祖先即为其父亲，而其k级祖先为k-1级祖先的父亲（k≥2）。例如，2级祖先即为父亲的父亲。现在你想知道一些生物的若干级父亲。
#
#
#
# 输入描述
# 第一行两个以空格给开的正整数n和q，表示生物总数和询问次数
#
# 第二行有n-1个由空格隔开的正整数，a2,a3,…an 依次表示2号生物的父亲、3号生物的父亲…i号生物的父亲的编号为ai。其中1号生物的父亲已经无法追踪到了。
#
# 接下来q行，每行两个由空格隔开的正整数 x , k ，表示询问第x号生物的k级祖先。
#
# n，q≤50000，1≤ ai < i ，1≤x, k≤n
#
# 输出描述
# 输出q行，每行依次对应一个询问的答案，即第x号生物的k级祖先。如果无法追踪到该祖先，则输出0
#
#
# 样例输入
# 5 3
# 1 2 3 4
# 5 1
# 1 1
# 5 3
# 样例输出
# 4
# 0
# 2
#
# 提示
# 第二次询问1号节点的1级祖先，即父亲，但1号节点的父亲已经无法追踪了，因而输出0
import sys

lines = sys.stdin.readline().strip()
n, q = list(map(int, lines.split()))
lines = sys.stdin.readline().strip()
a = list(map(int, lines.split()))
res = []

a_dic = {}
for i in range(len(a)):
    a_dic[i + 2] = a[i]


def cal(a_dic, q_in):
    x, k = q_in
    if x == 1:
        return 0
    if k == n:
        return 0
    for i in range(k):
        if x in a_dic:
            x = a_dic[x]
            if x == 1:
                if i == k - 1:
                    return 1
                else:
                    return 0
        else:
            return 0
    return x


for _ in range(q):
    lines = sys.stdin.readline().strip()
    q_in = list(map(int, lines.split()))
    res.append(cal(a_dic, q_in))

for i in res:
    print(i)
