#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:     
        #Solution 1:
        letters = {}
        palindrome_length = 0

        # Go through each letter and increment value in dictionary for each occurrence
        for letter in s:
            # Check if the letter is already in the dictionary
            # If not, set value to 1 occurrence
            if letter not in letters: letters[letter] = 1
            else: letters[letter] += 1
        
        for key in letters.keys():
            # Add each letter that occurred an even no. of times to the palindrome
            if letters[key]%2 == 0:
                palindrome_length += letters[key]
                letters[key] = 0
            else:
                palindrome_length += (letters[key]//2)*2
                letters[key] = 1
        
        # By now the palindrome length must be even,
        # so one more letter can be placed in the middle and it still be a palindrome
        for value in letters.values():
            # Look for odd values
            if value == 1:
                # Return length including one odd letter in the middle
                return (palindrome_length + 1)

        # If no odd values remain in the dictionary, return the even numbered length
        return palindrome_length

        # Solution 2:
        letters = [0] * 52 # 26 lowercase and 26 uppercase letters
        res = 0

        # 65-90 are ASCII values for A-Z
        # 97-122 are ASCII values for a-z
        for char in s:
            ascii = ord(char)
            if ascii >= 97: letters[ascii - 71] += 1
            else: letters[ascii-65] += 1
        
        # Add all even occurrences of letters to the palindrome
        odd_inserted = False # Flag to check if an odd letter has been inserted
        for letter in letters:
            res += letter - letter % 2
            if not odd_inserted and letter % 2 == 1:
                res += 1
                odd_inserted = True
        
        return res
# @lc code=end

