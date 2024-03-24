#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for n in nums:
            if n not in seen: seen.add(n)
            else: return n
        
# @lc code=end

