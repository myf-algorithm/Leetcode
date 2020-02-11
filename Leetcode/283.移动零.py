class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for i in range(len(nums)):
            if nums[i] != 0:    # 遇到非零元素
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

    def moveZeroes1(self, nums):
        loc = 0
        for num in nums:
            if num != 0:
                nums[loc] = num
                loc += 1
        while loc < len(nums):
            nums[loc] = 0
            loc += 1

