#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # find the index of ch in word
        index = None
        i = 0
        while index is None and i < len(word):
            if ch == word[i]: index = i
            i+=1
        # If ch is not in the word
        if index is None: return word

        # Reverse the prefix upto the index and add the remainder of the string
        return word[0:index+1][::-1] + word[index+1 : len(word)]
        
# @lc code=end

