# coding:utf-8
# 桶排序的序列需要满足下面两个特点：
#   1，待排序的所有值都处于一个可枚举的范围内
#   2，这个范围不能太大，否则排序的开销比较大

# 1.建立好对应的桶
# 2.把要排序的数组分别放入对应的桶中
# 3.统计元素在桶中出现的次数
# 4.按照桶的顺序输出桶里的元素

# 当桶的个数最大时，桶排序就是计数排序


def bucketSort(nums):
    # 选择一个最大的数
    max_num = max(nums)
    # 创建一个元素全是0的列表, 当做桶
    bucket = [0] * (max_num + 1)
    # 把所有元素放入桶中, 即把对应元素个数加一
    for i in nums:
        bucket[i] += 1
    # 存储排序好的元素
    sort_nums = []
    # 取出桶中的元素
    for j in range(len(bucket)):
        # 桶上为0就不统计了，不为0的时候继续
        if bucket[j] != 0:
            for y in range(bucket[j]):
                sort_nums.append(j)
    return sort_nums


nums = [5, 6, 3, 2, 1, 65, 2, 4, 8, 4]
print(bucketSort(nums))
