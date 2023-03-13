class Solution(object):
    def isPalindrome(self, s):
        s_filter = []
        for i in s:
            if i.isdigit() or i.isalpha():
                s_filter.append(i.lower())
        for i in range(len(s_filter) // 2):
            if s_filter[i] != s_filter[len(s_filter) - i - 1]:
                return False
        return True
