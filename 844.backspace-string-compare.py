#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Values are cached since they will be used often in the loop
        # and to prevent calling len() function multiple times which would increase runtime
        len_s, len_t = len(s), len(t)
        # Stores strings with characters removed
        newS = newT = ""
        
        # Find longer string and keep looping until both have been iterated over
        # This is so that we can go over both strings in one iteration
        # instead of having two different loops for each string
        for i in range(0, max( len(s), len(t))):
            # Make sure index is still in range, if not assign empty string
            c_s = s[i] if i<len_s else ""
            c_t = t[i] if i<len_t else ""

            # Append curr. char to string
            # If backspace, remove previous character and do not append anything this iteration
            if c_s != "#": newS += c_s
            else: newS = newS[:-1]

            if c_t != "#": newT += c_t
            else: newT = newT[:-1]

        # See if both processed strings match
        return True if newS == newT else False

                       
# @lc code=end

