class Solution(object):
    def firstMissingPositive(self, nums):
        for a in nums:  # 遍历每个座位，记当前坐着a号乘客
            while 0 < a <= len(nums) and a != nums[a - 1]:  # 乘客a是正票但坐错了! 其座位被 ta=nums[a-1]占了
                nums[a - 1], a = a, nums[a - 1]  # a和ta两人互换则a对号入座。此后ta相当于新的a，去找自己的座位（循环执行）
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1  # 找到首个没有对号入座的nums[i]!=i+1
        return len(nums) + 1  # 满座，返回N+1


if __name__ == '__main__':
    S = Solution()
    print(S.firstMissingPositive([1, 2, 0]))
