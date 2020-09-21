# _*_ encoding:utf-8 _*_
# 9.20 度小满笔试1
# 由于新冠肺炎疫情的爆发，小明养在宿舍的小昆虫已经很久很久都没有人管了。小昆虫已经饿的不行了，必须出来找东西吃，可是出来之后需要走出一个迷宫。小昆虫每次可以朝上、下、左、右四个方向之一走一步，且只要走出任意一条边界线即可逃出迷宫。这只小昆虫曾感染过X星的一种奇异病毒，目前还没有发现任何副作用，但是却拥有了一项特异功能——破坏障碍物。
#
# 假设小昆虫在一个N*M的迷宫中，"@"代表小昆虫的初始位置，"."代表可以通过的空地，"*"代表可以破坏的障碍物，"#"代表不可破坏的障碍物。请问小昆虫最少需要使用多少次特异功能才可以逃出迷宫？
#
#
#
# 输入描述
# 多组数据，第1行有1个正整数T，表示有T组数据。（T<=100）
#
# 对于每组数据，第1行有两个整数N和M。(1<=N, M<=1000)
#
# 接着N行，每行有一个长度为M的字符串，表示N*M的迷宫。
#
# 输出描述
# 输出一个整数，表示使用特异功能的最少次数。如果小昆虫不能走出迷宫，则输出-1。

# 3
# 3 3
# ###
# #@*
# ***
# 3 4
# ####
# #@.*
# **.*
# 3 3
# .#.
# #@#
# .#.

# 1
# 0
# -1

import sys

T = int(input())
for i in range(T):
    n, m = list(map(int, input().split()))
    l = []
    for i in range(n):
        l.append(list(input()))

for i in range(n):
    for j in range(m):
        if l[i][j] == '@':
            stack = [(i, j)]
            visited = {(i, j)}
            break
result = 0
ready = []
flag = False
while stack:
    temp = []
    for ni, nj in stack:
        if ni == 0 or ni == n - 1 or nj == 0 or nj == m - 1:
            flag = True
            break
        for ne_i, ne_j in [[ni + 1, nj], [ni - 1, nj], [ni, nj + 1], [ni, nj - 1]]:
            if (ne_i, ne_j) not in visited:
                if l[ne_i][ne_j] == '.':
                    temp.append((ne_i, ne_j))
                elif l[ne_i][ne_j] == '*':
                    ready.append((ne_i, ne_j))
                visited.add((ne_i, ne_j))
    if flag:
        break
    if not temp and not ready:
        result = -1
        break
    elif not temp:
        stack = ready[:]
        result += 1
        ready = []
    else:
        stack = temp[:]
print(result)
