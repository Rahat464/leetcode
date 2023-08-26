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

        # Iterate over each integer in list and subtract it from Sn
        for i in nums: Sn -= i
        
        # The misssing integer will be the remaining value
        return Sn
        
# @lc code=end

