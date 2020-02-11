class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp[n+1]=max(dp[n],dp[n−1]+num)
        dp[0]=0
        """
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur
        return cur

    def rob1(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[-1]

    def rob2(self, nums):
        if not nums:  # 空时直接返回 0
            return 0
        if len(nums) <= 2:  # 元素个数小于 2 时的最基本情况
            return max(nums)
        dp = [[None] * 2 for _ in nums]  # 初始化数组
        dp[0][0] = 0  # 第 1 天未抢
        dp[0][1] = nums[0]  # 第 1 天抢劫了
        for i in range(1, len(nums)):  # 从第二天开始择优
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        n = len(nums) - 1
        return max(dp[n][0], dp[n][1])  # 从最后一天选择出 抢了最后一天 和 没抢最后一天 最大的

    def robr(self, nums):
        import functools
        n = len(nums)

        @functools.lru_cache(None)
        def helper(i):
            if i >= n: return 0
            return max(helper(i + 1), nums[i] + helper(i + 2))

        return helper(0)


