class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1 and nums[0] == 0:
            return 1
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return nums[-1] + 1

    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [0, 2, 3]
        """
        nums.sort()
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1
        return left

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        0 - 3 + 1 - 0 + 2 - 1 + 3 - x = 0，求出 x = 2
        """
        res = len(nums)
        for idx, num in enumerate(nums):
            res += idx - num
        return res

    def missingNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        a ^ b ^ b = a
        """
        res = 0
        for idx, num in enumerate(nums):
            res = res ^ idx ^ num
        return res ^ len(nums)

