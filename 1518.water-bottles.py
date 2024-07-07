#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        empty = numBottles

        while empty >= numExchange:
            exchanged = empty // numExchange
            empty %= numExchange
            res += exchanged
            empty += exchanged
        
        return res
        
# @lc code=end

