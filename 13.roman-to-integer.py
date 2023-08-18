#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C" : 100,
            "D" : 500,
            "M": 1000}
        
        # Keeps a running total of the roman numerals
        total = 0

        # Iterate through each letter in string
        for i, c in enumerate(s):
            total += numerals[c]

            # Subtract values

            # Conditions: 
            # - i>=x to prevent IndexError
            # - Previous char can only be I,X or C
            # - Previous char must be smaller than current char
            if i>=1 and  s[i-1] in ("I","X","C") and numerals[s[i-1]]<numerals[c]:
                # *2 because the value has already been added, so it needs to be removed first then it needs to be subtracted
                total -= numerals[s[i-1]]*2
                    
                if i>=2 and s[i-2] in ("I","X") and numerals[s[i-2]]<numerals[c]:
                    total -= numerals[s[i-2]]*2
            
        return total
        
# @lc code=end

