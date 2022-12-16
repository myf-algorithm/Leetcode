class Solution(object):
    def maxSubArray(self, nums):
        # 以 nums[i] 为结尾的最大子数组和为 dp[i]
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)


if __name__ == '__main__':
    S = Solution()
    print(S.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
