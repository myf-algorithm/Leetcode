class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        res = 0
        for i in range(len(nums)):
            if vote == 0:
                res = nums[i]
                vote += 1
            else:
                if nums[i] == res:
                    vote += 1
                else:
                    vote -= 1
        return res
