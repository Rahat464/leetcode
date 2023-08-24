#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counts number of zero occurrences
        count = i = 0
        length = len(nums) # Cache length as it will be used often

        # Iterate over length-count, which is the normal length - no. of zeros known to be in nums
        while i < length-count:
            if nums[i] == 0:
                # Increment count and delete zero from array
                count += 1
                del nums[i]
            # Do not increment if 0 as curr. element will be deleted and i+1 will become i.
            # If it incremented every time, it would skip the element after the 0.
            else: i += 1
        
        # Add all zeros to the end of the list
        nums.extend([0]*count)
# @lc code=end

