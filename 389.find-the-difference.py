#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}
        for c in s:
            if c not in freq: freq[c] = 1
            else: freq[c] += 1
        
        for c in t:
            if c in freq and freq[c] > 0: freq[c] -= 1
            else: return c
        # for k, v in freq.items():
        #     if v < 0: return k
            
        
# @lc code=end

