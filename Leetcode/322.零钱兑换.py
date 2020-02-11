class Solution(object):
    def coinChange_dp(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        dp[i]表示金额为i需要最少的硬币
        dp[i] = min(dp[i], dp[i - coin[j]])
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min(dp[i - c] if i - c >= 0 else float('inf') for c in coins) + 1
        return dp[-1] if dp[-1] != float('inf') else -1

    def coinChange_bfs(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        from collections import deque
        queue = deque([amount])
        step = 0
        visited = set()
        while queue:
            n = len(queue)
            for _ in range(n):
                tmp = queue.pop()
                if tmp == 0:
                    return step
                for coin in coins:
                    if tmp >= coin and tmp - coin not in visited:
                        visited.add(tmp - coin)
                        queue.appendleft(tmp - coin)
            step += 1
        return -1

    def coinChange_dfs(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        self.res = float('inf')

        def dfs(i, num, amount):
            if amount == 0:
                self.res = min(self.res, num)
                return
            for j in range(i, len(coins)):
                if (self.res - num) * coins[j] < amount:
                    break
                if coins[j] > amount:
                    continue
                dfs(j, num + 1, amount - coins[j])

        for i in range(len(coins)):
            dfs(i, 0, amount)
        return self.res if self.res != float('inf') else -1
