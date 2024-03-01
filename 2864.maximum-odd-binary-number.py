#
# @lc app=leetcode id=2149 lang=python3
#
# [2864] Maximum Odd Binary Number
#

# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = 0
        zero_count = 0
        for char in s:
            if char == "1": one_count += 1
            else: zero_count += 1
        
        return ("1" * (one_count - 1)) + ("0" * zero_count) + "1"

# @lc code=end

