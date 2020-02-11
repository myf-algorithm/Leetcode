class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) / 2]

    def majorityElement_count(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        now = None  # 当下正在计数的元素
        for i in nums:
            if count == 0:
                now = i  # 被抵消没了，换下一个元素
            count += 1 if now == i else -1  # 计数
        return now  # 众数数量大于所有其他元素，最后一定是众数

    def majorityElement_dict(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        set1 = set(nums)
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for i in set1:
            if dic.get(i) > (len(nums) // 2):
                return i
