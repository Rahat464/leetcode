#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
# Regular expression used to remove all non alphanumeric chars
import re


class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        # convert all upper to lowercase and remove whitespace
        # use re library to remove all non-alphanumeric values including _
        palindrome = re.sub(r'\W+', '', s).lower().replace("_", "")

        length = len(palindrome)
        for i, letter in enumerate(palindrome):
            if letter != palindrome[length - 1 - i]:
                return False
            elif i==length-i:
                return True

        return True

        
# @lc code=end

