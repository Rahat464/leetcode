#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the root is none, it won't have any subtrees hence we can determine false
        if root is None: return False

        # dfs() is used to check if the root and subroot are the same, if not dfs() will immediately return false
        # isSubTree() is used twice to check both subtrees.
        # if dfs() returned false, it means we haven't replaced root with the correct subtree (.left or .right)
        # so we use recursion to call the function again and check with both subtrees.
        # If it keeps making recursive calls it will stop when the root has reached a leaf 
        # as that means the subRoot doesnt exist
        return self.dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def dfs(self, r: Optional[TreeNode], s: Optional[TreeNode]) ->bool:
        # if both are Null, they will be equal to eachother
        # Since we are checking if the subtrees are equal,
        # this will also check if the node is equal too 
        # since all the subtrees of this node and its value should be equal
        if r is s: return True
        # return false if one of them is null, meaning that one of them has reach the end when it wasn't supposed to
        # or if the values of the two nodes isn't the same, meaning that the subroot doesn't exist in this node
        elif r is None or s is None or r.val != s.val: return False
        
        # make a recursive call checking both left and right subtrees and return true
        # It will keep making recursive calls until it reaches Null, 
        # then it will keep returning true as long as values are equal
        # if either is false it means that subtrees below this aren't the subRoot
        return self.dfs(r.left, s.left) and self.dfs(r.right, s.right)
# @lc code=end