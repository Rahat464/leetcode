#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
    
        for word in words:
            if self.isPalindrome(word): return word

        return ""

    def isPalindrome(self, word):
        l = 0
        r = len(word) - 1

        while l<r:
            if word[l] != word[r]: return False
            l += 1
            r -= 1

        return True
        
# @lc code=end

