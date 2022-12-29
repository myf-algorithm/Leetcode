# trie tree，又称前缀树或字典树. 它利用字符串的公共前缀来节约存储空间
# 性质:
#   （1）根节点不包含字符，除根节点外的每个节点只包含一个字符。
#   （2）从根节点到某一个节点，路径上经过的字符连接起来，为该节点对应的字符串。
#   （3）每个节点的所有子节点包含的字符串不相同。

# 应用:
#   词频统计
#   比直接用hash节省空间
#   搜索提示
#   输入前缀的时候提示可以构成的词
#   作为辅助结构
#   如后缀树，AC自动机等的辅助结构

# 实现:
# 虽然python没有指针,但是可以用嵌套字典来实现树结构，对于非ascii的单词,统一用unicode编码来插入与搜索

from collections import defaultdict


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = defaultdict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("_end")

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "_end" in current:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert('hello')
    trie.insert('nice')
    trie.insert('to')
    trie.insert('meet')
    trie.insert('you')
    print(trie.search('hello'))
