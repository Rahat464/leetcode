#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            if (node is None): return
            if (node.children):
                for c in node.children:
                    dfs(c)
            res.append(node.val)
        
        res = []
        dfs(root)
        return res

        
# @lc code=end

