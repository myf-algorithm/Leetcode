# coding:utf-8
# 希尔排序是插入排序的一种，也叫缩小增量排序
# 希尔排序时间复杂度会比O(n^2)好一点，空间复杂度为O(1)
# 相同的元素在各自的组内进行插入排序，可能会发生移动，所以是不稳定的


def shell_sort(alist):
    """希尔排序"""
    # n=9
    n = len(alist)
    # gap = 4
    gap = n // 2  # 初始步长，gap取整数
    # i = gap
    # for i in range(gap, n):
    #     # i = [gap, gap+1, gap+2, gap+3... n-1]
    #     while:
    #     if alist[i] < alist[i-gap]:
    #         alist[i], alist[i-gap] = alist[i-gap], alist[i]

    # gap变化到0之前，插入算法执行的次数
    while gap > 0:
        # 插入算法，与普通的插入算法的区别就是gap步长
        for j in range(gap, n):
            # j = [gap, gap+1, gap+2, gap+3, ..., n-1]
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        print(gap)
        print(alist)
        # 缩短gap步长
        gap //= 2


if __name__ == "__main__":
    # li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    li = ['S', 'H', 'E', 'L', 'L', 'S', 'O', 'R', 'T', 'I', 'S', 'U', 'S', 'E', 'F', 'U', 'L']
    print(li)
    shell_sort(li)
    print(li)
