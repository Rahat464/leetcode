#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = None
        i = 0

        while increasing is None:
            if i+1 < len(nums):
                if nums[i] < nums[i+1]: increasing = True
                elif nums[i] > nums[i+1]: increasing = False
                else: i += 1
            else: return True

        prev = nums[0]

        if increasing is True:
            for n in nums[i:]:
                if n < prev: return False
                else: prev = n
        else:
            for n in nums[i:]:
                if n > prev: return False
                else: prev = n
        
        return True
        
# @lc code=end

