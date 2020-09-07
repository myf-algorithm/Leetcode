class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

    def findPeakElement1(self, nums):
        l, r = 1, len(nums)
        nums = [float('-inf')] + nums + [float('-inf')]
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m - 1
            elif nums[m] < nums[m - 1]:
                r = m - 1
            else:
                l = m + 1
        return l - 1


class Solution_traverse:
    def solve(self, a):
        # write code here
        n = len(a)
        if n == 1:
            return 0
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                if a[i] >= a[i - 1]:
                    return i
            elif i == 0:
                if a[i] >= a[i + 1]:
                    return i
            else:
                if a[i] >= a[i - 1] and a[i] >= a[i + 1]:
                    return i
        return -1
