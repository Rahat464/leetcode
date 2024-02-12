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
        # DFS Solution
        if not root: return 0

        depth : int = 0
        q : list = [root]
        while q:
            depth += 1
            for _ in range(len(q)):
                node = q[0]
                del q[0]
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        return depth


    #     # Deal with empty trees
    #     if not root: return 0

    #     # + 1 accounts for root node
    #     # max() finds the larger subtree among left and right
    #     return 1 + max(self.dfs(root.left), self.dfs(root.right))

    # def dfs(self, root):
        
    #     if not root: return 0
        
    #     '''
    #     - 1+ accounts for current node
    #     - self.dfs returns the largest subtree between left/right
    #     - The leaves will return 1, its parents return 1+1 etc...
    #       and that makes up the depth of the l/r subtree
    #     '''
    #     l = 1 + self.dfs(root.left)
    #     r = 1 + self.dfs(root.right)

    #     # max() finds the larger subtree among left and right
    #     return max(l, r)
# @lc code=end