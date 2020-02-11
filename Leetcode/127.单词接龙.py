class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import defaultdict
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:  # 遍历列表中的单词
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        queue = [(beginWord, 1)]  # Queue for DFS
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)  # 取出队列中的第一个元素
            for i in range(L):  # 循环第一个单词长度
                inter_word = current_word[:i] + "*" + current_word[i + 1:]
                for word in all_combo_dict[inter_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[inter_word] = []
        return 0


if __name__ == '__main__':
    S = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(S.ladderLength(beginWord, endWord, wordList))
