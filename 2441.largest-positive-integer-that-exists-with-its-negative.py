#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        res = -1

        for n in nums:
            if -n not in seen: seen.add(n)
            else: res = max(res, abs(n))
        
        return res

        
# @lc code=end

