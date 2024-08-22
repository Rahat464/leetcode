#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
# import math
class Solution:
    def findComplement(self, num: int) -> int:
        log = math.log2(num)
        if log.is_integer(): return int((2**log) - 1)
        return (2**math.ceil(log)) - num - 1
        
# @lc code=end

