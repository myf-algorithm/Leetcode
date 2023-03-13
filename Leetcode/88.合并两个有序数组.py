class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        双指针，从后往前
        时间复杂度 : O(n+m)
        空间复杂度 : O(1)
        """
        p1 = m - 1  # for num1
        p2 = n - 1  # for num2
        p = n + m - 1  # for num1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]

    def merge1(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        nums1[:] = []

        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        if p1 < m:
            nums1[p1 + p2:] = nums1_copy[p1:]
        else:
            nums1[p1 + p2:] = nums2[p2:]


if __name__ == '__main__':
    S = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    S.merge(nums1, m, nums2, n)
    print(nums1)
