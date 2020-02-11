"""
给定n个字符串，请对n个字符串按照字典序排列。
"""

s = []
n = int(input())
for i in range(n):
    s.append(input())
# sorted(s)
s.sort()
for i in s:
    print(i)


