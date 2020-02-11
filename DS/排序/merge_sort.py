# coding:utf-8
# 归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。
# 将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。
# 然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。

# 归并算法：时间复杂度为O(nlogn)，空间复杂度为O(n)，稳定的


def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2

    # left 采用归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])

    # right 采用归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid:])

    # 将两个有序的子序列合并为一个新的整体
    # merge(left, right)
    left_pointer, right_pointer = 0, 0
    result = []

    # 左边或者右边的其中一个已经走到头
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    # 添加没有走到头的那个序列
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    sorted_li = merge_sort(li)
    print(li)
    print(sorted_li)

    # merge_sort   [54, 26, 93, 17, 77, 31, 44, 55, 20]
    #
    # left_li = merge_sort [54, 26, 93, 17]
    #
    #     left_li = merge_sort [54, 26]
    #     left_li = [26, 54]
    #
    #
    #              left_li = [54]
    #              right_li = [26]
    #              result = [26, 54]
    #              return result
    #
    #     right_li = merge_sort([93, 17])
    #
    #             left_li = merge_sort([93])
    #
    #                         return [93]
    #             left_li =[93]
    #
    #             right_li = merge_sort([17])
    #
    #                         return [17]
    #             right_li = [17]
    #
    #             result = [17, 93]
    #
    #             return result
    #
    #     right_li = [17, 93]
    #
    #     result = [17, 26, 54, 93]
    #
    #     return result
    #
    # left_li = [17, 26, 54, 93]
    #
    # right_li = merge_sort([77, 31, 44, 55, 20])
    #
    #
    # result = []
    # return result
