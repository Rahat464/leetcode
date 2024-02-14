#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS with variable to keep track of largest number found so far
        return self.dfs(root, root.val)
    
    def dfs(self, root, max_val):
        if not root: return 0
        count = 1 if root.val >= max_val else 0
        max_val = max(max_val, root.val)
        return count + self.dfs(root.left, max_val) + self.dfs(root.right, max_val)
        
# @lc code=end

