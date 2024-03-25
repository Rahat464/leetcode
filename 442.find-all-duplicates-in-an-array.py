#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Time complexity: O(n)
        # Space complexity: O(1) assuming input list is not considered as extra space
        res = []
        for n in nums:
            index = abs(n) - 1
            if nums[index] < 0: res.append(abs(index) + 1)
            else: nums[index] *= -1
        return res
        
# @lc code=end

