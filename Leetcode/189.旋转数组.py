class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())

    def rotate1(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

    def rotate2(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

