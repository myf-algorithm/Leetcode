class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            index = i
            for j in range(len(needle)):
                if haystack[index] == needle[j]:
                    index += 1
                else:
                    break
                if index - i == len(needle):
                    return i
        return -1

    def strStr1(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr1(haystack="aaa", needle="a"))
