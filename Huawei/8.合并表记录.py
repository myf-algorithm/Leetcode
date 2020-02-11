"""
 数据表记录包含表索引和数值，请对表索引相同的记录进行合并，
 即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
 数据表记录包含表索引和数值，请对表索引相同的记录进行合并，
 即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
"""

n = int(input())
res = dict()
while True:
    try:
        for i in range(n):
            k, v = map(int, input().split())  # 输入每行用空格隔开的两个数字
            if k not in res:
                res[k] = v
            else:
                res[k] += v
        sorted(res)
        for k in res.keys():
            print(k, res[k])
    except:
        break
