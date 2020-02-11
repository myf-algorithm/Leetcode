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
