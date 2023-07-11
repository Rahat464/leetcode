#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # If the root node is Null, return true since there are no nodes hence it is balanced
        if not root:
            return True
        
        if abs(self.height(root.left) - self.height(root.right)) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False

    def height(self, node):
        # Check if null
        if not node:
            return False
        
        # Make recursive height() call for both right and left branches
        # Check which branch is larger using max()
        # Add 1 to that and return it
        return 1 + max(
            self.height(node.right),
            self.height(node.left))
        

        
# @lc code=end

