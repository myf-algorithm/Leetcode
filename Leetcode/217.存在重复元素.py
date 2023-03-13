class Solution(object):
    def containsDuplicate(self, nums):
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False
