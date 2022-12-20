class Solution(object):
    def rob(self, nums):
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
        return dp[0]
