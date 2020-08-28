# coding:utf-8
# 快速排序是对冒泡排序的改良，又称划分交换排序（partition-exchange sort）
# 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
# 然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

# 步骤为：
#     从数列中挑出一个元素，称为"基准"（pivot）。
#     重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
#           在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
#     递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

# 递归的最底部情形，是数列的大小是零或一，也就是永远都已经被排序好了。
# 虽然一直递归下去，但是这个算法总会结束，因为在每次的迭代（iteration）中，
# 它至少会把一个元素摆到它最后的位置去。

# 快速排序最优时间复杂度：O(nlogn)，最坏时间复杂度：时间复杂度O(n^2)，空间复杂度：O(logn)-O(n)，不稳定


def quick_sort(alist, first, last):
    """快速排序"""
    # 递归的退出条件
    if first >= last:
        return
    # 设定待排序序列的起始元素为基准元素
    mid_value = alist[first]
    # low为序列左边的由左向右移动的游标
    low = first
    # high为序列右边由右向左移动的游标
    high = last
    while low < high:
        # 如果low与high未重合，并且high指向的元素不比基准元素小，high左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        # 若high指向的元素小于基准值，则将high指向的元素放在low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，并且low指向的元素比基准元素小，low右移
        while low < high and alist[low] < mid_value:
            low += 1
        # 若low指向的元素小于基准值，则将low指向的元素放在high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid_value

    # 对low左边的列表执行快速排序
    quick_sort(alist, first, low - 1)

    # 对low右边的列表排序
    quick_sort(alist, low + 1, last)


def quick_sort_simple(nums):
    if len(nums) < 2:
        return nums
    left = quick_sort_simple([i for i in nums[1:] if i <= nums[0]])
    right = quick_sort_simple([j for j in nums[1:] if j > nums[0]])
    return left + [nums[0]] + right


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
    print(quick_sort_simple(li))
