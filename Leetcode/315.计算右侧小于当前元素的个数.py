class BinaryIndexedTree:
    def __init__(self, nums):
        self.BIT_arr = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.BIT_arr[i + 1] = nums[i]
        for i in range(1, len(self.BIT_arr)):
            j = i + (i & -i)
            if j < len(self.BIT_arr):
                self.BIT_arr[j] += self.BIT_arr[i]

    # 更新,是指在i位置上加上 val
    def updata(self, i, delta):
        i += 1
        while i < len(self.BIT_arr):
            self.BIT_arr[i] += delta
            i += (i & (-i))

    # 重新赋值, 在i位置为val
    def setVal(self, i, val):
        i += 1
        self.updata(i, val - self.BIT_arr[i])

    def prefix(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.BIT_arr[i]
            i -= (i & (-i))
        return res


class SegmentTree(object):
    def __init__(self, nums):
        self.l = len(nums)
        self.tree = [0] * self.l + nums
        for i in range(self.l - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    # 重新赋值, 在i位置为val
    def setVal(self, i, val):
        n = self.l + i
        self.tree[n] = val
        while n > 1:
            self.tree[n >> 1] = self.tree[n] + self.tree[n ^ 1]
            n >>= 1

    # 更新,是指在i位置上加上 val
    def updata(self, i, val):
        n = self.l + i
        tmp = self.tree[n]
        self.setVal(i, tmp + val)

    def sumRange(self, i, j):
        m = self.l + i
        n = self.l + j
        res = 0
        while m <= n:
            if m & 1:
                res += self.tree[m]
                m += 1
            m >>= 1
            if n & 1 == 0:
                res += self.tree[n]
                n -= 1
            n >>= 1
        return res


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.leftSum = 0
        self.dup = 0


class Solution(object):
    def countSmaller_2div(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        queue = []
        res = []
        for num in nums[::-1]:
            loc = bisect.bisect_left(queue, num)
            res.append(loc)
            queue.insert(loc, num)
        return res[::-1]

    def countSmaller_merge_sort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        res = [0] * len(nums)
        for idx, num in enumerate(nums):
            arr.append((idx, num))

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            tmp = []
            i = 0
            j = 0
            while i < len(left) or j < len(right):
                if j == len(right) or i < len(left) and left[i][1] <= right[j][1]:
                    tmp.append(left[i])
                    res[left[i][0]] += j
                    i += 1
                else:
                    tmp.append(right[j])
                    j += 1
            return tmp

        merge_sort(arr)
        return res

    def countSmaller_Fenwick_Tree(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        树状数组：Binary Indexed Tree(B.I.T), Fenwick Tree
        """
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}
        tree = BinaryIndexedTree([0] * len(hashTable))
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(tree.prefix(hashTable[nums[i]] - 1))
            tree.updata(hashTable[nums[i]], 1)
        return res[::-1]

    def countSmaller_Segment_Tree(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        线段树: segment tree
        """
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}
        tree, r = SegmentTree(len(hashTable) * [0]), []
        for i in range(len(nums) - 1, -1, -1):
            r.append(tree.sumRange(0, hashTable[nums[i]] - 1))
            tree.updata(hashTable[nums[i]], 1)
        return r[::-1]

    def countSmaller_BST(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        二叉树: BST
        """

        def insert(node, val):
            Sum = 0
            while node.val != val:
                if node.val > val:
                    if node.left == None:
                        node.left = Node(val)
                    node.leftSum += 1
                    node = node.left
                else:
                    Sum += node.leftSum + node.dup
                    if node.right == None:
                        node.right = Node(val)
                    node = node.right
            node.dup += 1
            return Sum + node.leftSum

        if not nums:
            return []
        res = [0] * len(nums)
        root = Node(nums[-1])
        for i in range(len(nums) - 1, -1, -1):
            res[i] = insert(root, nums[i])
        return res
