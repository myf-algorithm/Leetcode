# 选择排序（Selection sort）是一种简单直观的排序算法。
# 它的工作原理如下：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 以此类推，直到所有元素均排序完毕。
#
# 选择排序的主要优点与数据移动有关。
# 如果某个元素位于正确的最终位置上，则它不会被移动。
# 选择排序每次交换一对元素，它们当中至少有一个将被移到其最终位置上，因此对n个元素的表进行排序总共进行至多n-1次交换。
# 在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。

# 最优时间复杂度：O(n^2)，最坏时间复杂度：O(n^2)，稳定性：不稳定（考虑升序每次选择最大的情况）


def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n - 1):  # j: 0 ~ n-2
        min_index = j
        # 依次在剩余序列里面寻找最小值
        for i in range(j + 1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        # 找到后放在已排好序列的末尾
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)
