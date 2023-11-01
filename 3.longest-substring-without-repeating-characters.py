#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        res, curr, l = 0, 0, 0

        for c in s:
            while c in char:
                char.remove(s[l])
                l +=1
                curr -= 1
            
            char.add(c)
            curr += 1
            res = max(res, curr)
        
        return res
        
# @lc code=end

