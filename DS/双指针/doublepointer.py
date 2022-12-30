# 双指针主要用于遍历数组，两个指针指向不同的元素，从而协同完成任务。


class Solution:
    def twosum(self, nums, target):
        i, j = 0, len(nums) - 1
        while i < j:
            sum = nums[i] + nums[j]
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            else:
                return [i + 1, j + 1]
        return None

    def judgeSquareSum(self, target):
        i, j = 0, int(target ** 0.5)
        while i <= j:
            sum = i * i + j * j
            if sum < target:
                i += 1
            elif sum > target:
                j -= 1
            else:
                return True
        return False

    def reverseVowels(self, s: str):
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s) - 1
        s = list(s)
        while i < j:
            if s[i] in vowel and s[j] in vowel:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1
            elif s[i] not in vowel:
                i = i + 1
            elif s[j] not in vowel:
                j = j - 1
        return ''.join(s)

    def validPalindrome(self, strs):
        i, j = 0, len(strs) - 1
        while i < j:
            if strs[i] != strs[j]:
                return self.isPalindrome(strs, i, j - 1) | self.isPalindrome(strs, i + 1, j)
            i += 1
            j -= 1
        return True

    def isPalindrome(self, strs, left, right):
        while left < right:
            if strs[left] != strs[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    S = Solution()
    print(S.twosum([1, 2, 3, 4, 5, 6], 4))
    print(S.judgeSquareSum(5))
    print(S.reverseVowels('hfahfahgaisghoia'))
    print(S.validPalindrome('aba'))
