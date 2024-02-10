#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)

        for length in range(2, len(s)): #O(n)
            for i in range(0, len(s)): # O(n)
                if i+length <= len(s):
                    substring = s[i:i+length]
                    if self.isPalindrome(substring): res += 1
    
        if len(s) == 1: return res
        return (res+1) if self.isPalindrome(s) else res

    def isPalindrome(self, substring):
        l = 0
        r = len(substring) - 1

        while l<r:
            if substring[l] != substring[r]:
                return False
            l+=1
            r-=1

        return True
        
# @lc code=end

