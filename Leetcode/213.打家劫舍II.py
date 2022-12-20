def rob(nums: List[int]) -> int:
    def robRange(nums):
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
        return dp[0]

    n = len(nums)
    if n == 1:
        return nums[0]
    return max(robRange(nums[:n - 1]), robRange(nums[1:]))