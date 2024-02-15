#
# @lc app=leetcode id=2971 lang=python3
#
# [2971] Find Polygon With the Largest Perimeter
#

# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Thanks Neetcode
        nums.sort()
        curr_total = sum(nums[0:2])
        curr_max = -1

        for n in range(2, len(nums)):
            if curr_total > nums[n]: curr_max = curr_total + nums[n]
            curr_total += nums[n]
        
        return curr_max

# @lc code=end

