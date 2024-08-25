#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(node):
            if node is None: return
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            res.append(node.val)
        
        res = []
        dfs(root)
        return res


        
# @lc code=end