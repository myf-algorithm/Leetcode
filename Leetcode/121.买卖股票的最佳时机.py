class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

    def maxProfit_dp(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        首先构造diff数组，求连续两天的价格差
        状态转移方程dp[i] = max(dp[i - 1] + diff[i], 0), dp[i]指以i元素结尾的子数组的最大和
        接着遍历diff数组，根据状态转移方程求出dp数组
        最后dp数组中的最大值就是最大价格差
        """
        if len(prices) <= 1:
            return 0
        diff = [0 for _ in range(len(prices) - 1)]
        for i in range(len(prices) - 1):
            diff[i] = prices[i + 1] - prices[i]
        dp = [0 for _ in range(len(prices) - 1)]
        dp[0] = max(0, diff[0])
        max_profit = dp[0]
        for i in range(1, len(prices) - 1):
            dp[i] = max(0, diff[i] + dp[i - 1])
            max_profit = max(max_profit, dp[i])
        return max_profit

    def maxProfit_dp1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        用一个临时变量代替dp
        """
        if len(prices) <= 1:
            return 0
        diff = [0 for _ in range(len(prices) - 1)]
        for i in range(len(prices) - 1):
            diff[i] = prices[i + 1] - prices[i]
        temp = max_profit = 0
        for i in range(len(prices) - 1):
            temp = max(0, diff[i] + temp)
            max_profit = max(max_profit, temp)
        return max_profit

    def maxProfit_dp2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        diff数组其实也没有必要
        """
        temp = max_profit = 0
        for i in range(len(prices) - 1):
            temp = max(0, prices[i + 1] - prices[i] + temp)
            max_profit = max(max_profit, temp)
        return max_profit


if __name__ == '__main__':
    S = Solution()
    print(S.maxProfit([7, 1, 5, 3, 6, 4]))
