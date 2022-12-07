# 单调栈 + 哈希表
def nextGreaterElement(self, nums1, nums2):
    res = {}
    stack = []
    for num in reversed(nums2):
        while stack and num >= stack[-1]:
            stack.pop()
        res[num] = stack[-1] if stack else -1
        stack.append(num)
    return [res[num] for num in nums1]