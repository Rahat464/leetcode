#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Check if list is empty
        if not nums: return -1

        l = 0
        r = len(nums) - 1

        
        while (l<=r):
            midpoint = round( (l+r)/2 )
            
            # If midpoint is the target
            if nums[midpoint] == target:
                return midpoint
            # If midpoint is larger than target
            elif nums[midpoint] > target:
                r = midpoint - 1
            # If midpoint is too small
            else:
                l = midpoint + 1

        return -1
        
# @lc code=end

