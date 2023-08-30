#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Original solution was to sort, then square each value
        # Thanks neetcode for better O(n) solution

        # pointers keep track of next number to square on each side
        l, r= 0, len(nums) - 1
        #points at previous index to be filled with squared value
        prev = len(nums) - 1
        # new list created to store squared values
        squared = [0] * len(nums)

        # Keep looping as long as l pointer is behind or equal to r, 
        # meaning that there are still values to be squared
        while l<=r:
            # if value at l pointer is larger, fill prev index with that
            if abs(nums[l]) > abs(nums[r]):
                squared[prev] = nums[l] ** 2
                # then increment pointer to point to next value 
                l += 1
            else:
                squared[prev] = nums[r] ** 2
                r -= 1
            
            # decrement pointer so that squared values aren't overwritten
            prev -= 1

        return squared
        
# @lc code=end
