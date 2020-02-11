import math
C1, C2 = list(map(int, input().strip().split()))
T = (C2 - C1) / 100
shi = int(T // 3600)
fen = int((T - shi * 3600) // 60)
miao_floor = math.floor(T - shi * 3600 - fen * 60)
num = T - shi * 3600 - fen * 60 - miao_floor
if num < 0.5:
    miao = miao_floor
else:
    miao = miao_floor + 1
print("{:0>2}".format(shi) + ':' + "{:0>2}".format(fen) + ':' + "{:0>2}".format(miao))
