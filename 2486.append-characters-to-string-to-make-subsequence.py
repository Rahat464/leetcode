#
# @lc app=leetcode id=2486 lang=python3
#
# [2486] Append Characters to String to Make Subsequence
#

# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ptr = 0 # Pointer to char in t
        # Iterate through the word, looking for the  ptr'th character in t
        for char in s:
            if ptr < len(t) and char == t[ptr]:
                ptr += 1
        
        return len(t) - ptr
        
# @lc code=end

