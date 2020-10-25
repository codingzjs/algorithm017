#-*- encoding:utf-8 -*-

#作业

#242.有效的字母异位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sset = set(s)
        if sset == set(t):
            for i in sset:
                if s.count(i) != t.count(i):
                    return False
            return True
        else:
            return False

#1.两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, nums_one in enumerate(nums):
            nums_two = target - nums_one
            if nums_two in dic:
                return [dic[nums_two], index]
            dic[nums_one] = index
        return None

#589.N叉树的前序遍历
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        def dfs(root, res):
            if not root:
                return
            res.append(root.val)
            if not root.children:
                return
            for child in root.children:
                dfs(child,res)
        res = []
        dfs(root, res)
        return res

#49.字母异位词分组
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in dic:
                dic[key] = [s]
            else:
                dic[key].append(s)
        return list(dic.values())

#94.二叉树的中序遍历
#递归，时间复杂度较高
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

#144.二叉树的前序遍历
#递归
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
#栈
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GRAY, node))
            else:
                res.append(node.val)
        return res

#N叉树的层序遍历
#丑数
#前K个高频元素
