#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        left: int = 1 if s[0] == '0' else 0
        right: int = 0

        for i in range(1, len(s)):
            if s[i] == '1': right += 1

        max_score: int = left + right

        for i in range(1, len(s) - 1):
            if s[i] == '0': left += 1
            else: right -= 1
            max_score = max(max_score, left + right)

        return max_score
        
# @lc code=end

