#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # DFS
        if not root: return False
        even = False

        q = [root]

        while q:
            even = not even
            prev = None
            q_len = len(q)

            for _ in range(q_len): # Go through each level
                node = q.pop(0)

                if even:
                    if node.val % 2 == 0 or (prev and node.val <= prev): return False
                else:
                    if node.val % 2 == 1 or (prev and node.val >= prev): return False

                # Update prev
                prev = node.val

                # Queue child nodes
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        return True
        
# @lc code=end

