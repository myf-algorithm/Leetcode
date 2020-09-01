class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
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


class Solution1:
    def merge(self, A, m, B, n):
        if not A:
            return B
        if not B:
            return A
        while m > 0 and n > 0:
            if A[m - 1] > B[n - 1]:
                A[m + n - 1] = A[m - 1]
                m -= 1
            else:
                A[m + n - 1] = B[n - 1]
                n -= 1
        if n > 0:
            A[:n] = B[:n]
        return A


if __name__ == '__main__':
    S = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    S.merge(nums1, m, nums2, n)
    print(nums1)
