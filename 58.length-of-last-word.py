#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = l = len(s) - 1

        # Deal with spaces at the end of the string
        while l >= 0 and s[l] == " ":
            r -= 1
            l -= 1
        
        while l >= 0 and s[l] != " ":
            l -= 1
        
        return r - l
        
# @lc code=end

