#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # 1st Solution
        # return sorted(s) == sorted(t)

        # 2nd Solution
        # Store the count of each character in dictionary
        letters = {}
        for char in s:
            if char in letters: letters[char] += 1
            else: letters[char] = 1
        
        # If the character is in t, decrement the count
        for char in t:
            if char in letters: letters[char] -= 1
            else: return False
        
        # Check that the count of each character is 0
        for value in letters.values():
            if value != 0: return False
        
        return True

        
# @lc code=end

