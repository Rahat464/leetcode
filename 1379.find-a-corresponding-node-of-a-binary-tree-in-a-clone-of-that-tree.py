#
# @lc app=leetcode id=1379 lang=python3
#
# [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # bfs

        if original is None: return
        elif original == target: return cloned

        res_l = self.getTargetCopy(original.left, cloned.left, target)
        if res_l is None:
            res_r = self.getTargetCopy(original.right, cloned.right, target)
            return res_r
        else: return res_l 
        
# @lc code=end

