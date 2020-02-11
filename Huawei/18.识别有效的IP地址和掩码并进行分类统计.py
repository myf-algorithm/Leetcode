import sys

num_A = 0
num_B = 0
num_C = 0
num_D = 0
num_E = 0
num_F = 0
num_G = 0


def check_ip(ip):
    if len(ip) != 4 or '' in ip:
        return False
    else:
        for i in range(4):
            if int(ip[i]) < 0 or int(ip[i]) > 255:
                return False
        else:
            return True


def bi(num):
    list1 = []
    while num:
        n = num % 2
        num = int(num / 2)
        list1.append(n)
    if len(list1) < 8:
        list1.append(0)
    list1.reverse()
    return list1


# 掩码是否正确，错误返回true
def judge_Ip(sm):
    sm = [int(i) for i in sm]
    list2 = []
    for i in range(4):
        list3 = bi(sm[i])
        list2.append(list3)
    list2 = sum(list2, [])
    n = 0
    for j in range(32):
        if list2[j] == 0:
            n = j
            break
    for j in list2[n:32]:
        if j == 1:
            return False
    return True


while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break
    line5 = line.split("~")[0]
    line6 = line.split("~")[1]
    line3 = line5.split(".")
    line4 = line6.split(".")

    # A B C D E码和私码
    if check_ip(line3) and judge_Ip(line4) and len(line4) == 4:
        line1 = [int(i) for i in line3]
        if 0 <= line1[1] <= 255 and 0 <= line1[2] <= 255 and 0 <= line1[3] <= 255:
            if line1[0] == 10:
                num_G += 1
            if 1 <= line1[0] <= 126:
                num_A += 1
            if 128 <= line1[0] <= 191:
                num_B += 1
            if 192 <= line1[0] <= 223:
                num_C += 1
            if 224 <= line1[0] <= 239:
                num_D += 1
            if 240 <= line1[0] <= 255:
                num_E += 1
        # 私码
        if 0 <= line1[2] <= 255 and 0 <= line1[3] <= 255:
            if line1[0] == 172 and 16 <= line1[1] <= 31:
                num_G += 1
            if line1[0] == 192 and line1[1] == 168:
                num_G += 1
    else:
        num_F += 1
print(num_A, num_B, num_C, num_D, num_E, num_F, num_G)
