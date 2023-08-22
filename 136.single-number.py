#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}

        # Iterates through list, adds new numbers to d, delete duplicate
        for n in nums:
            if n not in d: d[n] = 0
            else: del d[n]

        # Iterate through dict and find key with empty value
        for key, value in d.items():
            if value==0: return key

        
# @lc code=end