class Solution:
    def findMedianinTwoSortedAray(self, arr1, arr2):
        if not arr1 or not arr2:
            return -1
        l1, r1, l2, r2 = 0, len(arr1) - 1, 0, len(arr2) - 1
        m1 = (len(arr1) - 1) // 2
        m2 = m1
        l = 0
        while l1 < r1:
            m1 = (l1 + r1) // 2
            m2 = (l2 + r2) // 2
            l = r1 - l1 + 1
            if arr1[m1] > arr2[m2]:
                r1 = m1
                if l % 2 == 0:
                    l2 = m2 + 1
                else:
                    l2 = m2
            elif arr1[m1] < arr2[m2]:
                if l % 2 == 0:
                    l1 = m1 + 1
                else:
                    l1 = m1
                r2 = m2
            else:
                return arr2[m2]
        return min(arr1[l1], arr2[l2])


if __name__ == '__main__':
    s = Solution()
    nums1, nums2 = [1, 3, 4, 5], [2]
    print(s.findMedianinTwoSortedAray(nums1, nums2))
