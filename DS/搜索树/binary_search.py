# 对有序序列进行查找，分治的思想


def binary_search(list, num):
    left = 0
    right = len(list) - 1
    while left <= right:  # 循环条件
        mid = (left + right) // 2  # 获取中间位置，数字的索引（序列前提是有序的）
        if num < list[mid]:  # 如果查询数字比中间数字小，那就去二分后的左边找，
            right = mid - 1  # 来到左边后，需要将右变的边界换为mid-1
        elif num > list[mid]:  # 如果查询数字比中间数字大，那么去二分后的右边找
            left = mid + 1  # 来到右边后，需要将左边的边界换为mid+1
        else:
            return mid  # 如果查询数字刚好为中间值，返回该值得索引
    return -1  # 如果循环结束，左边大于了右边，代表没有找到


def binary_search_rec(list, left, right, num):
    if left > right:  # 递归结束条件
        return -1
    mid = (left + right) // 2
    if num < list[mid]:
        right = mid - 1
    elif num > list[mid]:
        left = mid + 1
    else:
        return mid
    return binary_search_rec(list, left, right, num)
    # 这里之所以会有return是因为必须要接收值，不然返回None
    # 回溯到最后一层的时候，如果没有return，那么将会返回None


# 对于表长较大，分布比较均匀的查找表来说，平均性能优于折半查找
# 对于分布不均匀的数据，折半查找比较好
def binary_search_insert(list, num):
    length = len(list)
    low = 0
    heigth = length - 1
    time = 0
    while low <= heigth:
        time += 1
        # 插值计算公式
        # 根据离所求值得距离进行切分
        mid = low + int((heigth - low) * (num - list[low]) / (list[heigth] - list[low]))
        if num > list[mid]:
            low = mid + 1
        elif num < list[mid]:
            heigth = mid - 1
        else:
            print("times: %s" % time)
            return mid


# 斐波那契查找，更准确地猜测寻找的值落在那个区间
def binary_search_fib(list, num):
    # 生成斐波那契数列
    fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)
    key = 0
    while fib(key) < len(list):
        key += 1

    left = 0
    right = len(list) - 1
    while left <= right:
        # 当x在分隔的后半部分时，fib计算的mid值可能大于arr长度
        # 计算fib的值，这个值是大于等于list的长度的，所以使用时要对key-1
        mid = min(left + fib(key - 1) - 1, len(list) - 1)  # 这里fib(key-1)-1的-1其实就是去掉索引重复值
        if num < list[mid]:  # 查找值小于分割记录
            right = mid - 1
            key -= 1
        elif num > list[mid]:  # 查找值大于分割记录
            left = mid + 1
            key -= 2
        else:  # 查找值等于分割记录
            return mid
    return -1


# 寻找与给定值最接近的数，若有多个返回最小的
def binary_search_value(list, num):
    if list[0] > num:  # 要查找小于最小值，返回最小值
        return list[0]
    if list[len(list) - 1] < num:  # 要查找大于最大值，返回最大值
        return list[len(list) - 1]
    left = 0
    right = len(list) - 1
    while left < right - 1:
        mid = (left + right) // 2
        if num < list[mid]:
            right = mid
        elif num > list[mid]:
            left = mid
        elif num == list[mid]:
            return list[mid]
    if (num - list[left]) <= (list[right] - num):
        return list[left]
    else:
        return list[right]


if __name__ == '__main__':
    list = [11, 32, 51, 21, 42, 9, 5, 6, 7, 8]
    print(list)
    list.sort()
    print(list)
    num = int(input('输入要查找的数：'))
    # res = binary_search(list, num)
    # res = binary_search_rec(list, 0, len(lis) - 1, num)
    # res = binary_search_insert(list, num)
    res = binary_search_fib(list, num)
    # res = binary_search_value(list, num)
    print(res)
    if res == -1:
        print('未找到！')
    else:
        print('找到！')
