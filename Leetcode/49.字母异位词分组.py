from typing import List


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        strs_sorted = []
        # 对输入列表中的每个字符串进行排序
        for s in strs:
            s = list(s)
            s.sort()
            strs_sorted.append("".join(s))
        # 将重复的字符串进行归类
        for i in range(len(strs_sorted)):
            if strs_sorted[i] not in dic:
                dic[strs_sorted[i]] = [strs[i]]
            else:
                dic[strs_sorted[i]].append(strs[i])
        # 返回结果列表
        return [value for value in dic.values()]



    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        """
        使用库函数
        """
        from collections import defaultdict
        lookup = defaultdict(list)
        for s in strs:
            lookup["".join(sorted(s))].append(s)
        return list(lookup.values())


if __name__ == '__main__':
    S = Solution()
    print(S.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
