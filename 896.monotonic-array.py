#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monotone = None
        i = 0
        prev = nums[0]

        while monotone is None:
            if i+1 < len(nums):
                if nums[i] < nums[i+1]: monotone = "increasing"
                elif nums[i] > nums[i+1]: monotone = "decreasing"
                else: i += 1
            else: return True

        if monotone == "increasing":
            for n in nums[i:]:
                if n < prev: return False
                else: prev = n
        else:
            for n in nums[i:]:
                if n > prev: return False
                else: prev = n
        
        return True
        
# @lc code=end

