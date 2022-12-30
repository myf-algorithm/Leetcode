# KMP算法是改进的高效的模式匹配算法，利用匹配失败后的信息，尽量减少模式串和主串的匹配次数，达到快速匹配的目的。
# 根据已有的信息，将比较的位置向后移动，提高效率。
# 每次移动的位置需要靠一个next数组来决定，这个next数组里面存储的就是匹配的信息。
# 原理解释：http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html


def getNextList(s):
    n = len(s)
    nextList = [0, 0]
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = nextList[j]
        if s[i] == s[j]:
            j += 1
        nextList.append(j)
    return nextList


def KMP(s, p):
    """
    Knuth-Morris-Pratt算法实现字符串查找
    """
    n = len(s)
    m = len(p)
    nextList = getNextList(p)
    indies = []
    j = 0
    for i in range(n):
        while s[i] != p[j] and j > 0:
            j = nextList[j]
        if s[i] == p[j]:
            j += 1
            if j == m:
                indies.append(i - m + 1)
                j = nextList[j]
    return indies


if __name__ == '__main__':
    # 测试
    s = 'ababababca'
    p = 'aba'
    print(KMP(s, p))
