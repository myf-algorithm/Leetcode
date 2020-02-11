class Solution(object):
    def maxProduct(self, nums):
        """
        记录前i的最小值, 和最大值
        dp[i] = max(nums[i] * pre_max, nums[i] * pre_min, nums[i])
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res

    def maxProduct_1(self, nums):
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)
