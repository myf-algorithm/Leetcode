# coding:utf-8

# 比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。
# 这步做完后，最后的元素会是最大的数。
# 针对所有的元素重复以上的步骤，除了最后一个。
# 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

# 稳定，时间复杂度O(n^2)，空间复杂度O(1)


def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            # 班长从头走到尾
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:  # 没有交换已经最优
            return


# [1, 2, 3 ,4 ,5, 6]


# i 0 ~ n-2   range(0, n-1) j=0
# i 0 ~ n-3   range(0, n-1-1) j=1
# i 0 ~ n-4   range(0, n-1-2) j=2
# j=n  i  range(0, n-1-j)
if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)

# for j in range(len(alist)-1,0,-1)
#
# [n-1, n-2, n-3, n-4,..., 1]
# for i in range(j)
#
# [0, 1, 2, 3,...,n-2]
# for i in range(n-1-j)
