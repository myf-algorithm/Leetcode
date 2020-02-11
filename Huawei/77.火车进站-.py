def handle(pre_station,in_station,after_station):
    """
    模拟栈操作，底部进，底部出，
    :param pre_station: 等待进站的车辆
    :param in_station:   已经在站里的车辆
    :param after_station:  已经出战的车辆
    :return:
    """
    if pre_station == [] and in_station == []:
        result.append(' '.join(after_station))
        return
    else:
        if in_station: # 站里有车，出战操作
            after_station.append(in_station.pop())
            handle(pre_station,in_station,after_station)
            in_station.append(after_station.pop())  # 一定记得还原操作现场
        if pre_station: # 未进站还有车，进站操作
            in_station.append(pre_station.pop(0))
            handle(pre_station,in_station,after_station)
            pre_station.insert(0,in_station.pop())
while True:
    try:
        result=[]
        count  = int(input())
        row = [i for i in input().split()]
        pre_station = row
        in_station = []
        after_station = []
        handle(pre_station,in_station,after_station)
        result.sort()
        for i in result:
            print(i)
    except:
        break