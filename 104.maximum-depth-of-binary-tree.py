#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right))

    def dfs(self, root):
        if not root: return 0 #something
        
        l = 1 + self.dfs(root.left)
        r = 1 + self.dfs(root.right)

        return max(l, r)
        

        
# @lc code=end

