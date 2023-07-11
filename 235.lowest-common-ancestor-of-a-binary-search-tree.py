#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        
        while root: # Will keep looping as long as root is not an empty node
            # If both (p,q) are smaller, move left
            if root.val > q.val and root.val > p.val:
                root = root.left
            
            # If both (p,q) are greater, move right
            elif root.val < q.val and root.val < p.val:
                root = root.right
            
            # If one is larger, and the other is smaller it means the current node is the LCA
            else:
                return root


# @lc code=end

