#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Deal with empty trees
        if root is None: return 0

        self.d = 0
        self.dfs(root)
        
        return self.d


    def dfs(self, root):
        # If the current node is empty, decrement to account for edge between root and null node.
        if not root: return -1

        l = self.dfs(root.left)
        r = self.dfs(root.right)

        # Update diameter
        # +2 accounts for edges between current node and its left and right child nodes
        self.d = max(self.d, l+r+2)

        # Find longer subtree and +1 to account for edge between parent node and curr node.
        return 1+ max(l, r)

    



        
# @lc code=end

