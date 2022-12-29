# --*-- coding: utf-8 --*--
# 计数排序是一个非基于比较的排序算法，优势在于在对一定范围内的整数排序时，快于基于比较的排序算法。
# 计数排序的基本思想在于给定的输入序列中的每一个元素x，确定该序列中值小于等于x元素的个数，
# 然后将x直接存放到最终的排序序列的正确位置上。

# 计数排序的时间复杂度：O(n+k)，空间复杂度O(n+k)，稳定的

# 当数列的最大和最小值差距过大时，并不适用计数排序
# 当数列元素不是整数，并不适用计数排序


def CountingSort(arr):
    # 检查入参类型
    if not isinstance(arr, (list)):
        raise TypeError('error para type')
    # 获取arr中的最大值和最小值
    maxNum = max(arr)
    minNum = min(arr)
    # 以最大值和最小值的差作为中间数组的长度，并构建中间数组，初始化为0
    # 中间数组用来统计arr中每个元素出现的次数，下标为arr元素的值，数组的值为下标值出现的次数
    length = maxNum - minNum + 1
    tempArr = [0 for i in range(length)]
    # 创建结果List，存放排序完成的结果
    resArr = list(range(len(arr)))
    # 第一次循环遍历，统计每个元素的出现次数，存入中间数组
    for num in arr:
        tempArr[num - minNum] += 1
    # 第二次循环遍历，遍历中间数组，每个位置的值 = 当前值 + 前一个位置的值，用来统计出小于等于当前下标的元素个数
    for j in range(1, length):
        tempArr[j] = tempArr[j] + tempArr[j - 1]
    # 第三次循环遍历，反向遍历arr的每个元素，找到该元素值在中间数组的对应下标，
    # 以这个中间数组的值作为结果数组的下标，将该元素存入结果数组
    for i in range(len(arr) - 1, -1, -1):
        resArr[tempArr[arr[i] - minNum] - 1] = arr[i]
        tempArr[arr[i] - minNum] -= 1
    return resArr


if __name__ == '__main__':
    arr = [12, 25, 26, 13, 14, 25, 12, 17, 18, 14]
    print(CountingSort(arr))
