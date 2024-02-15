#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        left = right = 0

        for i in range(0, len(nums)):
            #left side
            if i%2==0:left = max(left+nums[i], right)
            else: right = max(right+nums[i], left)
        
        return max(left, right)
        
# @lc code=end

