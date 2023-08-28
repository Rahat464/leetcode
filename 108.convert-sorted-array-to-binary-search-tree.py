#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #
        """
        This solution is a divide and conquer approach.
        The solution starts with the original nums, and makes the midpoint value the root
        Then it partitions the subarray on the left of the midpoint to be the left child node and vice versa
        Each recursion, the subarray is passed accordingly so that each call the midpoint is made the root node
        and to determine the child nodes, the function is called recursively.
        The recursion for each branch stops when the sub array is empty i.e. when r<0
        """
        # Left pointer will always be 0 i.e. first index in array
        # right pointer is last item in list and is -1 to prevent out of bounds index and to prevent infinite recursion
        r = len(nums)-1
        # midpoint decides which node will be made root and where to split nums into l and r subarray
        midpoint = round(r/2)

        if r<0: return None
        
        root = TreeNode(nums[midpoint])
        root.left = self.sortedArrayToBST(nums[:midpoint])
        root.right = self.sortedArrayToBST(nums[midpoint+1:])

        return root
        
# @lc code=end

