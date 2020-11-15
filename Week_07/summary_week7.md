## 第七周学习笔记

### Trie树的特点
1. 根节点不包含字符， 除根节点外每一个节点都只包含一个字符。

2. 从根节点到某一节点， 路径上经过的字符连接起来， 为该节点对应的字符串。

3. 在trie树中查找一个关键字的时间和树中包含的结点数无关， 而取决于组成关键字的字符数。 也就是查找字符串s的时间为O(len(s))
 

### Trie树的实现
```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#"
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True
```
### 相关题型

[211. 添加与搜索单词 - 数据结构设计](https://leetcode-cn.com/problems/design-add-and-search-words-data-structure/)

[212. 单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/)

[421. 数组中两个数的最大异或值](https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/)