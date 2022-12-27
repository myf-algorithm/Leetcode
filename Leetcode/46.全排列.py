class Solution(object):
    def permute(self, nums):
        res = []

        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res

    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        插入法
        """
        if len(nums) < 2:  # 如果为1个或两个元素直接返回
            return [nums]
        # 逐个元素的插入法，每次插入新元素到所有旧排列的所有能插入的位置生成新排列
        preres = [[nums[0]]]
        for i in nums[1:]:
            res = []
            for temp in preres:
                for j in range(len(temp) + 1):
                    res.append(temp[:j] + [i] + temp[j:])
            preres = res  # 成为旧排列
        return preres


if __name__ == '__main__':
    S = Solution()
    print(S.permute1([1, 2, 3]))
