#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Solution by Neetcode, couldn't figure out how to solve this without his video
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)    
    
    def dfs(self, l, r ):
        # If both l and r are empty, it means both are the same
        if l is r: return True
        # If one of them is empty, but the other isn't it means they're not equal
        # Both cannot be empty as that case has been taken care of by the if case above
        elif not l or not r: return False

        # The values of the l.l and r.r value is the same
        # Then check l.l against r.r, then l.r and r.l
        return (l.val == r.val) and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)

# @lc code=end

