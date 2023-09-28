#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # start & finish pointer point at respective ends of list
        s = 0
        f = len(nums) - 1
        
        # Keep looping until pointers meet
        # meaning that each end of the list has been iterated over
        while s < f:
            # If s or f is in place (even, odd) increment/decrement pointer and move on
            if nums[s] % 2 == 0: s += 1
            elif nums[f] % 2 != 0: f -= 1
            # if s is odd and f is even, swap them and decrement f as it is now odd
            else:
                nums[s], nums[f] = nums[f], nums[s]
                f -= 1
        
        return nums
        
# @lc code=end

