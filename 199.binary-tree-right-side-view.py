#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Breadth First Search
        # Append Rightmost value for each level if not null

        # Base Case
        if not root: return []

        res = []
        q = [root]

        while q:
            # Append left most value if not None
            rightmost_node = len(q) - 1
            while rightmost_node >= 0:
                if q[rightmost_node]:
                    res.append(q[rightmost_node].val)
                    break
                
                rightmost_node -= 1

            # We want to pop every node from the top-most level
            # So that we can get all nodes on the next level and then decide which to add to res
            curr_level_len = len(q) # Counts how many nodes left to pop
            for _ in range(curr_level_len):
                # Dequeue
                node = q[0]
                del q[0]

                # Enqueue other nodes
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        return res
        
# @lc code=end

