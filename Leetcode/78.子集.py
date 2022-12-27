from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法
        """
        size = len(nums)
        if size == 0:
            return []
        res = []
        self.__dfs(nums, 0, [], res)
        return res

    def __dfs(self, nums, start, path, res):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            # 因为 nums 不包含重复元素，并且每一个元素只能使用一次
            # 所以下一次搜索从 i + 1 开始
            self.__dfs(nums, i + 1, path, res)
            path.pop()

    def subsets_mask(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        n = 1 << size
        res = []
        for i in range(n):
            cur = []
            for j in range(size):
                if i >> j & 1:
                    cur.append(nums[j])
            res.append(cur)
        return res


S = Solution1()
S.subsets([1, 2, 3])
