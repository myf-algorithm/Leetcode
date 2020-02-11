class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if not nums:
        #     return False
        # nums.sort()
        # l = nums[0]
        # for i in nums[1:]:
        #     if i == l:
        #         return True
        #     else:
        #         l = i
        # return False

        visited = set()
        for num in nums:
            if num in visited: return True
            visited.add(num)
        return False
