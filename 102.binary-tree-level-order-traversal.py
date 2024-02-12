#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Base case, empty tree
        if not root: return []
        
        res : list = [[root.val]]
        q : list = [root]
        
        while q:
            level : list = []
        
            remaining = len(q)
            for _ in range(0, remaining):
                # Dequeue node
                node = q[0]
                del q[0]

                # Append
                if node.left:
                    q.append(node.left)
                    level.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    level.append(node.right.val)
                
            if level: res.append(level)
            
        return res
        
# @lc code=end

