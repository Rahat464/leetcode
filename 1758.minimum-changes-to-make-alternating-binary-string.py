#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        # Counts the number of changes needed to make the string alternating
        changes = 0

        for i in range(len(s)):
            if (i % 2 == 0 and s[i] == '1') or (i % 2 == 1 and s[i] == '0'):
                changes += 1
        
        return min(changes, len(s) - changes)
# @lc code=end

