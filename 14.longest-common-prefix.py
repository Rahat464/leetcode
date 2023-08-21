#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        # len(min(strs, key=len)) finds the length of the shortest string in strs
        # So the for loop will only loop until the shortest word is iterated over,
        # as any proceding character will not be a prefix.
        for c in range(len(min(strs, key=len))):
            # indicates if an odd character hasn't been found
            equal = True
            
            # Check the ith character of every string in the list
            for i in range(1, len(strs)):

                # If all the characters aren't equal to eachother
                # update flag accordingly and stop for loop
                if strs[i][c] != strs[i-1][c]:
                    equal = False
                    break
            
            # if equal hasn't been changed it means the current character is a prefix
            # if changed, it means an odd character has been found thus stop the loop
            if equal: prefix += strs[0][c] # append current char to end of string
            else: break
        
        return prefix
        
# @lc code=end

