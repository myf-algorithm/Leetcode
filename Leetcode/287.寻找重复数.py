class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        a = nums[0]
        for i in nums[1:]:
            if i == a:
                return a
            else:
                a = i

    def findDuplicate_2div(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:  # 计数，找小于等于mid的个数
                if num <= mid:
                    cnt += 1
            if cnt <= mid:  # <= 说明 重复元素再右半边
                left = mid + 1
            else:
                right = mid
        return left

    def findDuplicate_2point(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        # 当快慢指针相遇时，一定在环内。
        # 此时假设slow走了k步，则fast走了2k步。
        # 设环的周长为c，则k%c==0
        while slow != fast:  # 相等时，退出循环
            slow = nums[slow]  # 每次走一步
            fast = nums[nums[fast]]  # 每次走两步

        slow = 0
        # 假设起点到环的入口(重复元素)，需要m步。此时slow走了n+m步，
        # 其中n是环的周长c的整数倍，所以相当于slow走了m步到达入口，
        # 再走了n步。所以相遇时一定是环的入口。
        while slow != fast:  # 两个指针相遇时，退出循环
            slow = nums[slow]
            fast = nums[fast]
        return slow
