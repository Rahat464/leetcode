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
            # If the index is even, the character should be 0
            # If the index is odd, the character should be 1
            # If the character is not what it should be, we need to change it
            if (i % 2 == 0 and s[i] == '1') or (i % 2 == 1 and s[i] == '0'):
                changes += 1
        
        # We already know the minimum number of changes if the string started with 0
        # We can find the complement and compare the number of changes needed
        return min(changes, len(s) - changes)
# @lc code=end

