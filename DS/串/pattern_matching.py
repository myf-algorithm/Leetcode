def string_match(string, sub_str):
    # 蛮力法字符串匹配，算法时间复杂度为O(mn),m为文本字符串长度，n为模式子串长度
    for i in range(len(string) - len(sub_str) + 1):
        index = i  # index指向下一个待比较的字符
        for j in range(len(sub_str)):
            if string[index] == sub_str[j]:
                index += 1
            else:
                break
            if index - i == len(sub_str):
                return i
    return -1


# 首尾模式匹配算法对简单模式匹配算法的改进，匹配的次数要少一半
def FrontRearIndex(T, P):
    pos = 0
    startPos = pos
    long_t = len(T)
    long_p = len(P)
    while startPos < (long_t - long_p + 1):
        front = 0
        rear = len(P) - 1
        while front < rear:
            if (T[startPos + front] != P[front] or T[startPos + rear] != P[rear]):
                break
            else:
                front += 1
                rear -= 1
        if front > rear:
            return startPos
        else:
            startPos += 1
    return -1


if __name__ == '__main__':
    print(FrontRearIndex('adbcbdc', 'dc'))


