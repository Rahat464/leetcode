#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Use arithmetic series formula to calculate sum of all integers between 0 to n
        Sn = int((n + 1) * (n / 2))
        
        # The misssing integer will be the remaining value
        # sum() is used as it is more efficient than manually iterating over list
        return Sn - sum(nums)
        
# @lc code=end

