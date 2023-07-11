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

        # Store length as it will be needed multiple times
        length = len(palindrome)

        for i, letter in enumerate(palindrome):
            # if the current letter is not equal to the letter on the opposite end of the word
            if letter != palindrome[length - 1 - i]:
                return False
            # Check if the current letter is the middlemost letters
            # Words with even number length will have the last two letters next to each other e.g: le(tt)er
            # Whereas odd length words will have a middle letter word that will be compared to itself: o(d)d
            elif i==length-i:
                return True

        # If even length word, it will return here instead
        return True

        
# @lc code=end

