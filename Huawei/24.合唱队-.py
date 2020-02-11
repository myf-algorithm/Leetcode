import sys


def search(nums, target):
    low, high = 0, len(nums) - 1
    pos = len(nums)
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
            pos = high
    return pos


def deal(l, res):
    b = [9999] * len(l)
    b[0] = l[0]
    res = res + [1]
    for i in range(1, len(l)):
        pos = search(b, l[i])
        res += [pos + 1]
        b[pos] = l[i]
    return res


while True:
    try:
        n = int(input())
        queue = [int(c) for c in input().strip().split()]
        dp_1 = []
        dp_2 = []
        dp_1 = deal(queue, dp_1)
        queue.reverse()
        dp_2 = deal(queue, dp_2)
        dp_2.reverse()
        a = max([dp_1[i] + dp_2[i] for i in range(n)])
        print(n - a + 1)
    except:
        break
