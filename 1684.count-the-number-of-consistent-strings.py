#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set()
        res = 0
        
        for c in allowed: allowedSet.add(c)

        for word in words:
            shouldAdd = True
            
            cPtr = 0
            while shouldAdd and (cPtr < len(word)):
                if word[cPtr] not in allowedSet: shouldAdd = False
                cPtr += 1
            
            if (shouldAdd): res += 1
        
        return res
        
# @lc code=end

