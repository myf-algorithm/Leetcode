# 树状数组，也称作“二叉索引树”（Binary Indexed Tree）或 Fenwick 树。
# 它可以高效地实现如下两个操作：
#   1、数组前缀和的查询；
#   2、单点更新。
# 树状数组

class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0 for _ in range(n + 1)]

    def __lowbit(self, index):
        return index & (-index)

    # 单点更新：从下到上，最多到 size，可以取等
    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += self.__lowbit(index)

    # 区间查询：从上到下，最少到 1，可以取等
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.__lowbit(index)
        return res


class Solution(object):
    # 《剑指 Offer 》第 51 题：逆序数的计算
    # 在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
    # 输入一个数组，求出这个数组中的逆序对的总数。
    def inversePairs(self, nums):
        # 特判
        l = len(nums)
        if l < 2:
            return 0

        # 原始数组去除重复以后从小到大排序
        s = list(set(nums))

        # 构建最小堆，因为从小到大一个一个拿出来，用堆比较合适
        import heapq
        heapq.heapify(s)

        # 由数字查排名
        rank_map = dict()
        index = 1
        # 不重复数字的个数
        size = len(s)
        for _ in range(size):
            num = heapq.heappop(s)
            rank_map[num] = index
            index += 1

        res = 0
        # 树状数组只要不重复数字个数这么多空间就够了
        ft = FenwickTree(size)
        # 从后向前看，拿出一个数字来，就更新一下，然后向前查询比它小的个数
        for i in range(l - 1, -1, -1):
            rank = rank_map[nums[i]]
            ft.update(rank, 1)
            res += ft.query(rank - 1)
        return res

    # LeetCode第315题：计算右侧小于当前元素的个数
    # 给定一个整数数组nums，按要求返回一个新数组counts。
    # 数组counts有该性质：counts[i]的值是nums[i]右侧小于nums[i]的元素的数量。
    def countSmaller(self, nums):
        l = len(nums)
        if l == 0:
            return []
        if l == 1:
            return [0]

        s = list(set(nums))
        import heapq
        heapq.heapify(s)
        index = 1

        size = len(s)
        rank_map = dict()
        ft = FenwickTree(size)
        for _ in range(size):
            num = heapq.heappop(s)
            rank_map[num] = index
            index += 1

        # 从后向前填表
        res = [None for _ in range(l)]
        for index in range(l - 1, -1, -1):
            rank = rank_map[nums[index]]
            ft.update(rank, 1)
            res[index] = ft.query(rank - 1)
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.inversePairs([1, 2, 3, 4, 5, 6, 0]))
    print(S.countSmaller([5, 2, 6, 1]))
