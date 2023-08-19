#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Solution from Neetcode

        ans = nums[0] # Stores largest known sum
        sum = 0 # Stores running total
        
        for n in nums:
            # If the curr. sum is negative, restart sublist 
            if sum < 0: sum = 0
            sum += n

            # Update ans
            if ans < sum: ans = sum

        return ans
    

# @lc code=end

