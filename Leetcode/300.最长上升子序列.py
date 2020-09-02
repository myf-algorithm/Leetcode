class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        转移方程： dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)
        时间复杂度：O(N * N)
        空间复杂度：O(N)
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS_2div(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
        """
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            if j == res:
                res += 1
        return res


class Solution1:
    def LIS(self, arr):
        # write code here
        N = len(arr)
        res = [arr[0]]
        dp = [0] * N
        k = 1
        dp[0] = k

        def search(res, left, right, target):
            while left < right:
                mid = (left + right) >> 1
                if res[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        for i in range(1, N):
            if arr[i] > res[-1]:
                res.append(arr[i])
                k += 1
                dp[i] = k
            else:
                index = search(res, 0, k - 1, arr[i])
                res[index] = arr[i]
                dp[i] = index + 1

        ans = []
        prev = float('inf')
        for i in range(N - 1, -1, -1):
            if dp[i] == k and arr[i] < prev:
                ans.append(arr[i])
                k -= 1
                prev = arr[i]
        return ans[::-1]