#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    from collections import defaultdict

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Dictionary is used to keep count of occurrences of each letter in both words
        # collections library is used so that when a new key (letter) is mentioned, its value is set to 0
        l = defaultdict(int)

        # Iterate through first word and decrement count for each letter
        for letter in ransomNote:
            l[letter] -= 1

        # Iterate through second word and increment count for each letter
        for letter in magazine:
            l[letter] += 1
        
        # Iterate through each value in dictionary
        for v in l.values():
            # If any value is less than 0, it means that ransomNote has a letter that isn't in magazine
            if v<0:
                return False
            
        # If false, it would have already returned so by now, which means it must be true.
        return True

        
# @lc code=end

