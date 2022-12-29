# 基本思路：将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。
# 将其与末尾元素进行交换，此时末尾就为最大值，可称为有序区。然后将剩余n-1个元素重新构造成一个堆，估且称为堆区(未排序)。
# 这样会得到n个元素的次小值。重复执行，有序区从:1--->n，堆区：n-->0，便能得到一个有序序列了。

# coding=utf-8


def heap_adjust(array, start, end):
    temp = array[start]
    child = 2 * start
    while child <= end:
        if child < end and array[child] < array[child + 1]:
            child += 1
        if temp >= array[child]:
            break
        array[start] = array[child]
        start = child
        child *= 2
    array[start] = temp


def heap_sort(array):
    # 从最后一个有孩子结点的结点开始调整最大堆
    first = len(array) // 2 - 1
    for start in range(first, -1, -1):
        heap_adjust(array, start, len(array) - 1)

    # 将最大的数放到堆的最后一个位置，并继续调整排序
    for end in range(len(array) - 1, 0, -1):
        array[0], array[end] = array[end], array[0]
        heap_adjust(array, 0, end - 1)


if __name__ == "__main__":
    array = [1, 4, 5, 0, 2, 7, 9, 10, 3, 6]
    heap_sort(array)
    print(array)
