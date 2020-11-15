
#### 208. 实现 Trie (前缀树)
[leetcode#208-implement-trie-prefix-tree](https://leetcode-cn.com/problems/implement-trie-prefix-tree/submissions/)

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
#### 547. 朋友圈
[leetcode#547-friend-circles](https://leetcode-cn.com/problems/friend-circles/)

```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        count = 0
        visited = set()
        
        def dfs(i):
            for j in range(N):
                if M[i][j] and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        for i in range(N):
            if  i not in visited:
                count += 1
                visited.add(i)
                dfs(i)
        
        return count
```
