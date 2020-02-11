class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
            中心扩散的思路
            时间复杂度：O(N^2)
            空间复杂度：O(1)
        """
        size = len(s)
        if size == 0:
            return ''
        longest_palindrome = 1
        longest_palindrome_str = s[0]

        for i in range(size):
            # 最长回文子串的长度是奇数
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            # 最长回文子串的长度是偶数
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)
            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > longest_palindrome:
                longest_palindrome = len(cur_max_sub)
                longest_palindrome_str = cur_max_sub
        return longest_palindrome_str

    def __center_spread(self, s, size, left, right):
        """
        left = right的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        l = left
        r = right
        while l >= 0 and r < size and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r], r - l - 1

    def longestPalindrome_DP(self, s: str) -> str:
        """
            时间复杂度：O(N^2)
            空间复杂度：O(N^2)
        """
        if not s:
            return ""
        res = ""
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = float("-inf")
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                if dp[j][i] and max_len < i + 1 - j:
                    res = s[j: i + 1]
                    max_len = i + 1 - j
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome_DP('babad'))


