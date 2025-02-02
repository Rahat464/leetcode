#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        rotated: bool = False

        for i, n in enumerate(nums):
            if n < nums[i - 1]:
                if rotated: return False
                rotated = True

        return True
        
# @lc code=end

