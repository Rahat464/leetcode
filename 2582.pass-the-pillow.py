#
# @lc app=leetcode id=2582 lang=python3
#
# [2582] Pass the Pillow
#

# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time <  n: return time + 1
        
        # If rounds is even, then the flow is 0 -> len(n)
        # If odd, flow is len(n) -> 0
        rounds = time // (n - 1)
        if rounds % 2 == 0: return (time%(n-1) + 1)
        else: return (n - (time % (n-1)))
        
        
# @lc code=end

