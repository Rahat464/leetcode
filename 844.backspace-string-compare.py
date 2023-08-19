#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        newS = newT = ""
        
        for i in range(0, max( len(s), len(t))):
            c_s = s[i] if i<len_s else ""
            c_t = t[i] if i<len_t else ""

            if c_s != "#": newS += c_s
            else: newS = newS[:-1]

            if c_t != "#": newT += c_t
            else: newT = newT[:-1]

        return True if newS == newT else False

                       
# @lc code=end

