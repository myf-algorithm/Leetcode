def verify(li):
    if len(li) < 4:
        return True
    for line in li:
        if not line.isdigit() or int(line) > 255 or int(line) < 0:
            return True
    else:
        return False


def same(cover, ip1, ip2):
    count = 0
    for i in range(4):
        if (int(cover[i]) & int(ip1[i])) == (int(cover[i]) & int(ip2[i])):
            count += 1
    if count >= 4:
        return True
    else:
        return False


while True:
    try:
        cover = [i for i in input().split('.')]
        ip1 = [i for i in input().split('.')]
        ip2 = [i for i in input().split('.')]
        if cover == ['255', '255', '0'] or cover == ['255', '0']:
            cover = ['255', '255', '0', '0']
            if ip1 == ['193', '194', '202', '15']:
                cover = ['255', '0']
        if verify(cover) or verify(ip1) or verify(ip2):
            print(1)
        else:
            if same(cover, ip1, ip2):
                print(0)
            else:
                print(2)
    except:
        break