class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  # 蛮力法
        if not s:
            return 0
        max_lenth = 1
        for i in range(len(s)):
            sub_s = s[i]
            for j in range(i + 1, len(s)):
                if s[j] not in sub_s:
                    sub_s += s[j]
                    if len(sub_s) > max_lenth:
                        max_lenth = len(sub_s)
                else:
                    sub_s = ''
                    continue
        return max_lenth

    def lengthOfLongestSubstring1(self, s: str) -> int:  # 滑动窗口
        if not s:
            return 0
        left = 0
        max_l = 0
        for i in range(len(s)):
            if s[i] in s[left: i]:  # 发现当前元素s[i]出现过
                left += s[left: i].index(s[i]) + 1
            l = i - left + 1
            if l > max_l:
                max_l = l
        return max_l


if __name__ == '__main__':
    s = Solution()
    string = "pwwkew"
    print(s.lengthOfLongestSubstring(string))
