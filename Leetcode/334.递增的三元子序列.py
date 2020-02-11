class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num > second:
                return True
            if first > num:
                first = num
            elif first < num < second:
                second = num
        return False