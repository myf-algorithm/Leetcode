class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        分治算法
        """
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边的最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            # 递归计算右半边的最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

        # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        # 返回三个里面的最大值
        return max(max_right, max_left, max_l + max_r)

    def maxSubArray1(self, nums):
        """
        1. dp问题. 公式为: dp[i] = max(nums[i], nums[i] + dp[i - 1])
        2. 最大子序和 = 当前元素自身最大, 或者包含之前后最大
        动态规划
        """
        for i in range(1, len(nums)):
            # nums[i - 1]代表dp[i - 1]
            nums[i] = max(nums[i], nums[i] + nums[i - 1])

        return max(nums)


if __name__ == '__main__':
    S = Solution()
    print(S.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
