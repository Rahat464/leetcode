#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_letters = [float("inf")] * 26

        for j in range(len(words)):
            curr_word = [0] * 26
            for char in words[j]:
                curr_word[ord(char) - 97] += 1
            
            for i in range(len(common_letters)):
                common_letters[i] = min(common_letters[i], curr_word[i])

        res = []
        for i in range(len(common_letters)):
            if common_letters[i] != 0:
                res.extend([chr(97+i)] * common_letters[i])
        
        return res
        
# @lc code=end

